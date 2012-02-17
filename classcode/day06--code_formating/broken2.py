#!/usr/bin/env python
from random import randint
s=1
number=int(raw_input())
list1=[]

# create list with "number" of elements
for num in range(number):
    list1.append(randint(0,20))
print list1
#sort
while s:
    s=0
    for var in range(1,number):
        if list1[var-1]>list1[var]:
            t1=list1[var-1]
            t2=list1[var]
            list1[var-1]=t2
            list1[var]=t1
            s=1
print list1
