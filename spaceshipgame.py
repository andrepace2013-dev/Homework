import random
import pgzrun
WIDTH=500
HEIGHT=500
TITLE='space explorer'
score=0
game_over=False
spaceship=Actor('spaceship.png')
spaceship.pos=100,100
star=Actor('star.png')
star.pos=200,200
def draw():
    screen.blit("space",(0,0))
    spaceship.draw()
    star.draw()
    screen.draw.text("score: "+str(score),color="white",topleft=(10,10))
    if game_over:
        screen.fill('red')
        screen.draw.text("GAMEOVER, your final score is "+str(score),color="black",midtop=(WIDTH/2,220),fontsize=40)
def movestar():
    star.x=random.randint(0,500)
    star.y=random.randint(0,500)
def update():
    global score
    if keyboard.left:
        spaceship.x=spaceship.x-2
    if keyboard.right:
        spaceship.x=spaceship.x+2
    if keyboard.up:
        spaceship.y=spaceship.y-2
    if keyboard.down:
        spaceship.y=spaceship.y+2
    if spaceship.x>500:
         spaceship.x=300
         spaceship.y=300
    if spaceship.y>500:
         spaceship.x=300
         spaceship.y=300
    if spaceship.x<0:
         spaceship.x=300
         spaceship.y=300
    if spaceship.y<0:
         spaceship.x=300
         spaceship.y=300
    if spaceship.colliderect(star):
        score=score+10
        movestar()
def timeup():
    global game_over
    game_over=True
clock.schedule(timeup,60.0)
pgzrun.go()