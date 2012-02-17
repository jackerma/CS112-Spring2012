#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""

pile=int(40)
x=False
turn1=True
turn2=False
over="Invalid number of stones"
under="Not enough stones"
#explain set up
print "Number of stones in the pile:", pile
print "maximum number of stone per turn: 5"
#start game loop
while x!=True:
 #player1 loop
 while turn1==True:
  #player2 takes stones
  take1=int(raw_input(str(pile) + ' stones left. Player 1, [1-5]:'))
  #player2 takes stones
  if take1>5 or take1<1:
   print over
  #if # stones is greater than pile, deny
  elif take1>pile:
   print under
  #subtract stone from pile
  else:
   pile-=take1
   #switch turns
   turn2=True
   turn1=False
 #if pile is empty, end
 if pile==0:
  x=True
 else:
  #player2 loop
  while turn2==True:
   #player2 takes stones
   take2=int(raw_input(str(pile) + ' stones left. Player 2, [1-5]:'))
   #if # of stones is not 1-5, deny
   if take2>5 or take2<1:
    print over
   #if # stones is greater than pile, deny
   elif take2>pile:
    print under
   #subtract stone from pile
   else:
    pile-=take2
   #switch turns
   turn2=False
   turn1=True
 #if pile is empty, end
 if pile==0:
  x=True
if turn2==True:
 print "Player 2 won"
elif turn1==True:
 print "Player 1 won" 
