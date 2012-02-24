#!/usr/bin/env python

# Create a greeter
#    create a greeter that says hello to someone in all lower case.  Use print statements
#
#  ex:
#   >>> greeter("paul")
#   hello, paul
#   >>> greeter(3)
#   hello, 3
#   >>> greeter("WORLD")
#   hello, world

def greeter(name):
    if name== str(name):
        print "hello,", name.lower()
    else:
        print "hello,", name
greeter(raw_input("Name?"))

# Draw a box
#    given a width and a height, draw a box in the terminal.  Use print statements
#
#  ex:
#    >>> box("apples", -3)
#    Error: Invalid Dimensions
#    >>> box(1,1)
#    +
#    >>> box(4,2)
#    +--+
#    +--+
#    >>> box(3,3)
#    +-+
#    | |
#    +-+
error_msg = "Error: Invalid Dimensions"
def box(w,h):
    if w<1 or h<1:
        print error_msg, "1"
    elif int(w)!=w or int(h)!=h:
        print error_msg, "2"
    elif float(w)!=int(w) or float(h)!=int(h):
        print error_msg, "3"
    else:
        h=int(h)
        w=int(w)
        row1 = []
        for i in range(h):
            if i==0 or i==h-1:
                for i2 in range(w):
                    if i2==0 or i2==(w-1):
                        row1.insert(i2,"+")
                    else:
                        row1.insert(i2,"-")
            else:
                for i2 in range(w):
                    if i2==0 or i2==(w-1):
                        row1.insert(i2,"|")
                    else:
                        row1.insert(i2," ")
        
            print "".join(row1)
            
            row1=[]

box(int(raw_input("Width?")),int(raw_input("Height?")))


# ADVANCED
# Draw a Festive Tree
#    draw a festive tree based on the specifications.  You will need to discover the arguments 
#    and behavior by running the unittests to see where it fails.  Return a string, do not print.
#
#  ex:
#    >>> print tree()
#        *
#        ^
#       ^-^
#      ^-^-^
#     ^-^-^-^
#    ^-^-^-^-^
#       | |
#       | |

# def tree()

