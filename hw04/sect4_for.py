#!/usr/bin/env python
from hwtools import *

print "Section 4:  For Loops"
print "-----------------------------"

nums = input_nums()
# 1. What is the sum of all the numbers in nums?
a=0
for num in nums:
 a=num+a
print "1.", a


# 2. Print every even number in nums
print "2. even numbers"

#CODE GOES HERE

for num in nums:
 if num/2==num/2.0:
  print "", num
print ""

# 3. Does nums only contain even numbers? 
only_even = True

#CODE GOES HERE
for num in nums:
 if num/2!=num/2.0:
  only_even=False

print "3.",
if only_even:
 print "only even"
else:
 print "some odd"


# 4. Generate a list of every odd number less than 100. Hint: use range()
list1=[range(1,100,2)]
print "4.", list1

# 5. [ADVANCED]  Multiply each element in nums by its index

