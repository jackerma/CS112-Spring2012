#!/usr/bin/env python

import math

# Distance formula
#   calculate a function called "distance" to calculate the distance between two points.
#   http://www.purplemath.com/modules/distform.htm
#   ex: 
#      >>> distance((0,0), (3,4))
#      5

def distance(a, b):
    ax=int(a[0])
    ay=int(a[1])
    bx=int(b[0])
    by=int(b[1])
    d=math.sqrt((ax-bx)**2+(ay-by)**2)
    print d
a=[]
b=[]
c=raw_input("Enter x0: ")
d=raw_input("Enter y0: ")
e=raw_input("Enter x1: ")
f=raw_input("Enter y1: ")
a.append(c)
a.append(d)
b.append(e)
b.append(f)
distance(a, b)


# ADVANCED
# Normalizing Vectors
#   normalize a vector of length N.  If given all zeros, just spit back the same vector
#   http://www.fundza.com/vectors/normalize/index.html

#   ex:
#     >>> normalize((1,1))
#     [0.70710678118654746, 0.70710678118654746]
#     >>> normalize([0,0,0])
#     [0,0,0]
#     >>> normalize([1,1,1,1])
#     [0.25, 0.25, 0.25, 0.25]

# def normalize(vec):
    
