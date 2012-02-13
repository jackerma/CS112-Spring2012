#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""

a=int(40)
x=False
o=True
t=False
over="Invalid number of stones"
under="Not enough stones"
print "Number of stones in the pile:", a
print "maximum number of stone per turn: 5"
while x!=True:
 while o==True:
  s=int(raw_input(str(a) + ' stones left. Player 1, [1-5]:'))
  if s>5 or s<1:
   print over
  elif s>a:
   print under
  else:
   a-=s
  t=True
  o=False
 if a==0:
  x=True
 else:
  while t==True:
   s=int(raw_input(str(a) + ' stones left. Player 2, [1-5]:'))
   if s>5 or s<1:
    print over
   elif s>a:
    print under
   else:
    a-=s
   t=False
   o=True
 if a==0:
  x=True
if t==True:
 print "Player 2 won"
elif o==True:
 print "Player 1 won" 
