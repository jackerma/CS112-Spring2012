#!/usr/bin/env python
"""
multidim.py

Multidimensional Arrays
=========================================================
This section checks to make sure you can create, use, 
search, and manipulate a multidimensional array.
"""


# 1.  find_coins
#       find every coin (the number 1) in a givven room
#          room: a NxN grid which contains coins

#          returns: a list of the location of coind
#
#       Example:
#       0 0 0 1 0 0
#       0 0 1 0 0 0
#       0 0 0 0 1 0
#       0 0 0 0 0 0
# 
#       >>> find_coins(room)
#       [ [3, 0], [2, 1], [4, 2] ]
#      
def find_coins(room):
    global coins
    coins =[]
    k=0
    "returns a list of every coin in the room"
    for i in room:
        #row
        l=0
        for j in i:
            #col
            if j==1:
                coins.append((l,k))
            l+=1
            #next col/element
        k+=1
        #next row
    return coins

zeros = [ [0 for i in range(5)] for i in range(5) ]
find_coins(zeros)
print coins
diag = zeros[:]
diag[3][4] = 1
diag[0][1] = 1
diag[2][2] = 1
diag[4][1] = 1

find_coins(diag)

print coins



# 2. distance_from_player
#      calculate the distance from the player for each 
#      square in a room.  Returns a new grid of given
#      width and height where each square is the distance
#      from the player
import math
def distance_from_player(player_x, player_y, width, height):
    global grid
    "calculates the distance of each square from the player"
    grid = []
    for i in range(height):
        row=[]
        for j in range(width):
            row.append(1)
        grid.append(row)
    grid[player_x][player_y]=0

    k=0
    #row
    for i in grid:
        l=0
        #col
        for j in i:
            dist=0
            dist= math.sqrt((abs(k-player_x)**2)+(abs(l-player_y)**2))
            grid[k][l]=dist
            l+=1
            #next col/element
        k+=1
        #next row            
    return grid

    #print grid
    for i,row in enumerate(grid):
        for j, val in enumerate(row):
            print val,
        print ""


distance_from_player(1,1,7,5)
print grid
