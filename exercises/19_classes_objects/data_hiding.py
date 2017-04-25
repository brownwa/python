#!/usr/local/bin/python

# Sunday December 18, 2016
# data_hiding.py
# Waheed Brown
#
# References:
# https://www.tutorialspoint.com/python/python_classes_objects.htm

import sys
#import pdb; pdb.set_trace()

class JustCounter:
    __privateMember = 0

    # Default constructor is defined automatically
    # Only need define constructor if doing something special
    def __init__(self):
        self.__privateMember = 1
        self.__privateMethod()

    def __privateMethod(self):
        self.__privateMember += 10

    def count(self):
        self.__privateMember += 1
        print self.__privateMember

    def getCount(self):
        return self.__privateMember

def main(argv):
    counter = JustCounter()
    counter.count()
    counter.count()
    #print counter.__privateMember             # throws error b/c private member
    #print getattr(counter, "__privateMember") # throws error b/c private member
    #counter.__privateMethod()                 # throws error b/c private member
    print counter.getCount()

if __name__ == "__main__":
    main(sys.argv[1:])
