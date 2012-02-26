#!/usr/bin/env python
"""
tron.py

The simple game of tron with two players.  Press the space bar to start the game.  Player 1 (red) is controlled with WSAD and player 2 (blue) is controlled with the arrow keys.  Once the game is over, press space to reset and then again to restart.  Escape quits the program.
"""

import pygame
import pygame
from pygame import draw
from random import randrange
from pygame.locals import *

play1_x, play1_y = 0,300
play1_dx, play1_dy = 4,4
play2_x, play2_y = 800,300
play2_dx, play2_dy = 4,4
direc1= "x"
direc2= "nx"
s1=0
s2=0
#Draws player 1
def draw_play1(surf, pos, color=(50,50,255), size=4):
    x,y = pos
    width = size
    draw.rect(surf, color, (x, y, width, size))

#Draws player 2
def draw_play2(surf, pos, color=(255,50,50), size=4):
    x,y = pos
    width = size
    draw.rect(surf, color, (x, y, width, size))


def move(x, y, dx, dy, bounds, direction):
    if direction=="y":
        y+=dy
    elif direction=="ny":
        y+=-dy
    elif direction=="x":
        x+=dx
    elif direction=="nx":
        x+=-dx
    if x>bounds.right or x<bounds.left:
        done=True
    if y>bounds.bottom or y<bounds.top:
        done=True
    return x, y, dx, dy

pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
done = False
screen_bounds = screen.get_rect()
player1=[]
player2=[]
collis=[]
color=[]
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            done = True

#player1 move

        elif event.type == KEYDOWN and event.key == K_w:
            direc1="ny"
        elif event.type == KEYDOWN and event.key == K_s:
            direc1="y" 
        elif event.type == KEYDOWN and event.key == K_a:
            direc1="nx"
        elif event.type == KEYDOWN and event.key == K_d:
            direc1="x"

#player2 move

        elif event.type == KEYDOWN and event.key == K_UP:
            direc2="ny"
        elif event.type == KEYDOWN and event.key == K_DOWN:
            direc2="y"
        elif event.type == KEYDOWN and event.key == K_LEFT:
            direc2="nx"
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            direc2="x"

    screen.fill((0,0,0))
    play1_x, play1_y, play1_dx, play1_dy= move(play1_x, play1_y, play1_dx, play1_dy, screen_bounds,direc1)
    play2_x, play2_y, play2_dx, play2_dy= move(play2_x, play2_y, play2_dx, play2_dy, screen_bounds,direc2)


#draw player 1
    player1.append([play1_x, play1_y])
    color.append(255)
    for i in range(len(player1)):
        draw_play1(screen, player1[i], (0,0,color[i]))
    draw_play1(screen, [play1_x, play1_y])
    
#draw player 2
    player2.append([play2_x, play2_y])
    color.append(255)
    for i in range(len(player2)):
        draw_play2(screen, player2[i], (color[i],0,0))
    draw_play2(screen, [play2_x, play2_y])

#list for collisions (inc. self)
    for i in collis:
        if player1[-1]==i:
            done=True
            print "Player1 lost"
            s1+=1
        if player2[-1]==i:
            done=True
            print "Player2 lost"
            s2+=1

    collis.append([play1_x, play1_y])
    collis.append([play2_x, play2_y])

    pygame.display.flip()
    clock.tick(30)
    
print "Score:"
print "Player 1:", s1
print "Player 2:", s2
