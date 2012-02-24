#!/usr/bin/python env

# Calculate if a point is within a box
#    check if a point is inside a given box.  
#
#    Parameters:
#       pt: list of 2 numbers (x,y)
#       box: list of 4 numbers (x,y,w,h).  x,y is the top left point.  w,h is the width and height

def point_in_box(pt, box):
    right=box[0]+box[2]
    bottom=box[1]-box[3]
    top= box[1]
    left=box[0]
    if pt[0]<left or pt[0]>right:
        print "out of box"
    elif pt[1]>top or pt[1]<bottom:
        print "out of box"
    else:
        print ""
        print  "Point is in the box"
        
pt=[]
box=[]
pt.append(int(raw_input("Enter x of point")))
pt.append(int(raw_input("Enter y of point")))
box.append(int(raw_input("Enter x of box")))
box.append(int(raw_input("Enter y of box")))
box.append(int(raw_input("Enter width of box")))
box.append(int(raw_input("Enter height of box")))


point_in_box(pt, box)
