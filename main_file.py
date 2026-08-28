import pgzrun
import time
import random

WIDTH=800
HEIGHT = 600

START_SPEED =10
ITEMS = ["bag","battery","bottle","chips"] # non recy

FINAL_LEVEL=6
current_level=1
# lose the game
game_over=False
# win the game
game_complete=False

items = []
animations  = []

def draw():
    global items, current_level, game_complete, game_over
    screen.clear()
    screen.blit("bground",(0,0))

    if game_over:
        display_message("GAME OVER","Try again")
    elif game_complete:
        display_message("YOU WON!","well done.")
    else:
        for item in items:
            item.draw()
def display_message(heading,subheading):
    screen.draw.text(heading, fontsize=60, center=(400,300), color="black")
    screen.draw.text(subheading, fontsize=30, center=(400,330), color="black")


def update():
    global items
    if len(items) == 0:
        items     = make_items(current_level)
# make items
# 1. get the optins form items  list - random
# 2. create actors and add it to items l;ist 
# 3layout items - disply them with equal spacing
# animations - move objects down
pgzrun.go()