#!/usr/bin/env python

import pygame
from pygame.locals import *

## COLORS
BLUE = 0, 133, 199
RED = 223, 0, 36
YELLOW = 244, 195, 0
GREEN = 0, 159, 61
BLACK = 0, 0, 0
WHITE = 255, 255, 255

THICKNESS = 20


## MAIN
pygame.init()
screen = pygame.display.set_mode((800, 388))
pygame.display.set_caption("Olympic Rings   [press ESC to quit]")

## Draw
screen.fill(WHITE)

# blue ring
colorb=(100,100,255)
pos1=(150,125)
pygame.draw.circle(screen,colorb,pos1,115,20)

# black ring
colorbk=(0,0,0)
pos2=(400,125)
pygame.draw.circle(screen,colorbk,pos2,115,20)

#red ring
colorr=(205,0,0)
pos3=(650,125)
pygame.draw.circle(screen,colorr,pos3,115,20)

# yellow
colory=(255,205,0)
pos4=(275,250)
pygame.draw.circle(screen,colory,pos4,115,20)

# green ring
colorg=(0,175,0)
pos5=(525,250)
pygame.draw.circle(screen,colorg,pos5,115,20)

#################################
##  DRAW OLYPIC RINGS HERE
##
##  hint, lookup pygame.draw
##  specifically circle, ellipse,
##  and arc.  Also, the width
##  parameter
#################################


## Loop
clock = pygame.time.Clock()
done = False
while not done:
    event = pygame.event.poll()
    if event.type == QUIT:
        done = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
        done = True

    pygame.display.flip()
    clock.tick(30)

print "ByeBye"
