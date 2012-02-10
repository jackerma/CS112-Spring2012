#!/usr/bin/env python
from hwtools import *

print "Section 1:  If Statements"
print "-----------------------------"

# 1.  Is n even or odd?
n = raw_input("Enter a number: ")
n = int(n)

m=n/2
m=int(m)
b=n/2.0
b=int(b)
if m==b:
 a="odd"
else:
 a="even"
print "1.", a


# 2. If n is odd, double it
if a=="odd":
 v=n*2
 print "2.", n
else:
 print "2.", n, "(not odd)"

# 3. If n is evenly divisible by 3, add four
if n/3 == n/3.0:
 print "3.", n+4
else:
 print "3:", n, "(not multiple of 3)"


# 4. What is grade's letter value (eg. 90-100)
grade = raw_input("Enter a grade [0-100]: ")
grade = int(grade)
if grade>=90:
 c="A"
elif grade>=80:
 c="B"
elif grade>=70:
 c="C"
elif grade>=60:
 c="D"
else:
 c="F"
print "4.", c

