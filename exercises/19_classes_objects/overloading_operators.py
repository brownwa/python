#!/usr/local/bin/python

# Sunday December 18, 2016
# overloading_operators.py
# Waheed Brown
#
# References:
# https://www.tutorialspoint.com/python/python_classes_objects.htm

import sys

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        # % for strings is error prone for tuples and dictionaries
        # use str.format instead (with positional arguments)
        #
        # Reference:
        # https://infohost.nmt.edu/tcc/help/pubs/python/web/new-str-format.html

        #return "Vector (%d, %d)" % (self.a, self.b)
        return "Vector ({0}, {1})".format(self.a, self.b)

    def  __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

def main(argv):
    v1 = Vector(2, 10)
    v2 = Vector(5, -2)
    print v1 + v2

if __name__ == "__main__":
    main(sys.argv[1:])
