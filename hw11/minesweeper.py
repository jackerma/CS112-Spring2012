#!/usr/bin/env python

import pygame
from pygame import draw
from random import randrange
from pygame.locals import *
import random
import time

BACKGROUND = 0,0,0
RED=(255,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
TAN= (255,215,0)
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HIEGHT = 600, 600
FPS = 30
BOX_SIZE = 60, 60
GREY= (80,80,80)
BLACK=(0,0,0)
clickedlft = []
clickedrt = []
rects = []
underrects= []
values= []
mines= []
minescoord=[]
x,y=0,0
z=0
(255,215,0)
def draw_mines((x,y)):
    draw.rect(screen, TAN, (x-1, y-15, 2, 10))
    draw.circle(screen, GREY, (x, y), 10)
    draw.circle(screen, WHITE, (x-3, y-6), 2)
 


def draw_flag((x,y)):
    pole = pygame.Rect((x-5,y-20), (5,35))
    pygame.draw.rect(screen, BLACK, pole)
    pygame.draw.polygon(screen, RED, [(x,y-20),(x+20,y-10),(x,y)])


#mine pos
grid = [ [0 for i in range(10)] for i in range(10) ]
grid[randrange(0,10)][randrange(0, 10)] = 1
grid[randrange(0,10)][randrange(0, 10)] = 1
grid[randrange(0,10)][randrange(0, 10)] = 1
grid[randrange(0,10)][randrange(0, 10)] = 1
grid[randrange(0,10)][randrange(0, 10)] = 1
grid[randrange(0,10)][randrange(0, 10)] = 1
grid[randrange(0,10)][randrange(0, 10)] = 1
grid[randrange(0,10)][randrange(0, 10)] = 1
grid[randrange(0,10)][randrange(0, 10)] = 1
grid[randrange(0,10)][randrange(0, 10)] = 1


a=0

numbers= [ [0 for i in range(10)] for i in range(10) ]
k=0
for i in grid:
    #row
    l=0
    for j in i:
        #col
        if j==1:
            #creating grid
            if k<9 and l<9 and numbers[k+1][l+1]!="b" :
                a=numbers[k+1][l+1]
                a=a+1
                numbers[k+1][l+1]=a

            if  k<9 and numbers[k+1][l]!="b":
                a=numbers[k+1][l]
                a=a+1
                numbers[k+1][l]=a

            if  k<9 and numbers[k+1][l-1]!="b" and l!=0:
                a=numbers[k+1][l-1]
                a=a+1
                numbers[k+1][l-1]=a

            if l<9 and numbers[k][l+1]!="b":
                a=numbers[k][l+1] 
                a=a+1
                numbers[k][l+1]=a

            if numbers[k][l-1]!="b" and l!= 0:
                a=numbers[k][l-1] 
                a=a+1
                numbers[k][l-1]=a

            if l<9 and numbers[k-1][l+1]!="b" and k!=0:
                a=numbers[k-1][l+1] 
                a=a+1
                numbers[k-1][l+1]=a

            if numbers[k-1][l]!="b" and k!=0:
                a=numbers[k-1][l] 
                a=a+1
                numbers[k-1][l]=a

            if numbers[k-1][l-1]!="b"and k!=0 and l!=0:
                a=numbers[k-1][l-1] 
                a=a+1
                numbers[k-1][l-1]=a
                
            numbers[k][l]="b"
        l+=1
        #next col/element
    k+=1
    #next row
for i,row in enumerate(numbers):
    for j, val in enumerate(row):
        print val,
    print ""

#create grid
for i in range(0,600,60):
    for j in range(0,600,60):
        box = pygame.Rect((i,j),BOX_SIZE)
        rects.append(box)
        #creates underlayer
        underrects.append(box)
        values.append(numbers[i/60][j/60])
        if values[-1]== "b":
            mines.append(box)

#initiate pygame
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

#setup game objects

font= pygame.font.Font(None, 20)

#start game loop

done=False
while not done:

    #input

    for event in pygame.event.get():
        #quit
        if event.type == QUIT:
            done = True
        elif event.type == KEYDOWN and event.key== K_ESCAPE:
            done = True

        #click on box
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            for rect in rects:
                if rect.collidepoint(pygame.mouse.get_pos()) and rect not in clickedrt:
                    clickedlft.append(rect)
                    rects.remove(rect)
                    if rect in mines:
                        done=True
                    

        #flagging
        elif event.type == MOUSEBUTTONDOWN and event.button == 3:
            for rect in rects:
                if rect.collidepoint(pygame.mouse.get_pos()) and rect not in clickedlft:
                    if rect not in clickedrt:
                        clickedrt.append(rect)
                    elif rect in clickedrt:
                        clickedrt.remove(rect)

    #update

    #draw method

    screen.fill(BACKGROUND)
    
    #draw underlayer

 #   for rect in mines:
 #       draw_mine()

    for i in range(len(underrects)):
        if values[i]in range(1,9):
            text = font.render((str(values[i])), True, (RED),BLACK)
            loc = text.get_rect()
            loc.center = underrects[i].center
            screen.blit(text,loc)
    for rect in mines:
        
        if done==True:
            pygame.draw.rect(screen, RED, rect)
        draw_mines(rect.center)

    #draw grid overlay
    for rect in rects:
        if rect not in clickedlft and rect not in clickedrt and done==False:
            pygame.draw.rect(screen, GREY, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)
        elif rect in clickedrt and done==False:
            pygame.draw.rect(screen, GREY, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)

    for rect in clickedrt:
        if done!=True:
            draw_flag(rect.center)


    #refresh rate

    pygame.display.flip()
    clock.tick(FPS)

    if done==True:
        time.sleep(5)
