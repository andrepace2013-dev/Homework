from turtle import *
import time
import random
Score=0
w=Screen()
w.setup(width=500,height=300)
pen=Turtle()
pen.write('SELECT LEVEL \n IN TERMINAL',align='center',font=("Arial",45,"normal"))
rule=0
base=int(input("What level (1-5)"))
if base==1:
    rule=2
    pen.clear()
if base==2:
    rule=4
    pen.clear()
if base==3:
    rule=6
    pen.clear()
if base==4:
    rule=8
    pen.clear()
if base==5:
    rule=10
    pen.clear()
else:
    print("Invalid number")
dart=Turtle()
dart.shape('triangle')
dart.color('red')
dart.up()
dart.goto(0,-80)
dart.setheading(90)
baloons=[]
s=Turtle()
s.hideturtle()
s.penup()
s.goto(-145, 110)
def score():
    s.clear()
    s.write('Score:{}'.format(Score),font=("Arial",16,"normal"),align='right')
    print(score)
def game_over():
    over=Turtle()
    over.hideturtle()
    over.color('red')
    over.write('GAME OVER',align='center',font=("Arial",45,"normal"))
    print("GAME OVER")
    w.update()
    time.sleep(2)
    w.bye()
def makebaloon():
    baloon=Turtle()
    baloon.up()
    baloon.shape('square')
    colour=random.choice(['red','blue','green','yellow'])
    baloon.color(colour)
    x=random.randint(-150,150)
    baloon.goto(x,100)
    baloon.fall_speed = rule + random.uniform(1, 3)
    speed1=random.uniform(1,10)
    baloons.append(baloon)
def left():
    x=dart.xcor()
    if x>-150:
        dart.setx(x-10)
def right():
    x=dart.xcor()
    if x<150:
        dart.setx(x+10)
w.listen()
w.onkey(left,'Left')
w.onkey(right,'Right')
game_speed=0.02
difficulty=0.001
intervile = 0.5
last_spawn_time=time.time()
while True:
    w.update()
    current_time=time.time()
    if current_time-last_spawn_time>intervile:
        makebaloon()
        last_spawn_time=current_time
    for i in baloons[:]:
        i.sety(i.ycor() - i.fall_speed)
        if i.ycor()<-120:
            baloons.remove(i)
            Score+=10
            score()
            i.hideturtle()
        if dart.distance(i)<20:
            game_over()
            baloons.remove(i)
            i.hideturtle()
    game_speed=max(0.005,game_speed-difficulty)
    intervile=max(0.5,intervile-0.0005)
done()