#!/usr/local/bin/python

# Sunday December 18, 2016
# inheritance.py
# Waheed Brown
#
# References:
# https://www.tutorialspoint.com/python/python_classes_objects.htm

import sys

class Parent:
    parentAttr = 100

    def __init__(self):
        print "Calling parent constructor"

    def parentMethod(self):
        print "Calling parent method"

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "Parent attribute: ", Parent.parentAttr

class Aunt:
    auntAttr = 99

    def __init__(self):
        print "Calling aunt constructor"

class Child(Parent, Aunt):
    def __init__(self):
        print "Calling child constructor"

    def childMethod(self):
        print "Calling child method"

def main(argv):
    c = Child()
    c.childMethod()
    c.parentMethod()
    c.setAttr(200)
    c.getAttr()
    print "c.auntAttr = ", c.auntAttr

    return

if __name__ == "__main__":
    main(sys.argv[1:])
