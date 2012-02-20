#!/usr/bin/env python
"""
Selection sort

This is my selection sort, it's not working right!!!
I used this:
    http://en.wikipedia.org/wiki/Selection_sort
"""
from hwtools import input_nums

nums = input_nums()

print "Before sort:"
print nums

length=len(nums)
for number in range(length):
    first=number
    for second in range(number+1, length):
        if nums[second]<nums[first]:
            pos=second
            nums[second],nums[first]=nums[first],nums[second]

print "After sort:"
print nums
