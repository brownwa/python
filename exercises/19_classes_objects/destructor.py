#!/usr/local/bin/python

# Saturday December 17, 2016
# destructor.py
# Waheed Brown
#
# References:
# https://www.tutorialspoint.com/python/python_classes_objects.htm

import sys

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Destructor
    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"

def main(argv):
    pt1 = Point()
    pt2 = pt1
    pt3 = pt1

    print id(pt1), id(pt2), id(pt3) # prints IDs of objects

    del pt1
    del pt2
    del pt3

if __name__ == "__main__":
    main(sys.argv[1:])
