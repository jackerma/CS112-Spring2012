#!/usr/bin/env python
"""
Binary Search

This was supposed to be a binary search algorithm but it isn't working...
I used the Iterative implementation from here:
    http://en.wikipedia.org/wiki/Binary_search_algorithm
"""
from hwtools import input_nums

nums=input_nums()
nums=sorted(nums)
print "I have sorted your numbers"
find=int(raw_input("Which number should I find: "))
small=nums[0]-1
large=len(nums)-1
while large>=small:
    mid=int((large+small)/2)
    if nums[mid]==find:
        break
    elif find>nums[mid]:
       small=mid+1
    else:
        large-=1
if nums[mid]==find:
    print "Found", find, "at", mid
else:
    print "Could not find", find
