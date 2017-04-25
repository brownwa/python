#!/usr/local/bin/python

# Saturday February 6, 2016
# identity_operators.py
# Waheed Brown
#
# Python Tutorial
# http://www.tutorialspoint.com/python/identity_operators_example.htm

from ctypes import c_int, addressof
#import ctypes

# a = 20
# b = 20
a = False
b = 0
x = c_int(20)

print "a =", a, format( id(a), "016x" ) # Hex format
print "b =", b, format( id(b), "016x" )
print "addressof(x) =", format( addressof(x), "016x" ), "\n"

# NOTE: id() does not return the memory address of an object.
#       It only returns an integer guaranteed to be unique
#       for the object during its lifetime 
#
#       To get the actual memory address of an object, the
#       ctypes library needs to be imported. The addressof()
#       function can then be called.


if(a is b) :
    print "Line 1 - a and b have the same identity"
else :
    print "Line 1 - a and b do not have the same identity"

if( id(a) == id(b) ) :
    print "Line 2 - a and b have the same identity"
else :
    print "Line 2 - a and b do not have the same identity"

a = 30
b = 30

if(a is b) :
    print "Line 3 - a and b have same identity"
else :
    print "Line 3 - a and b do not have same identity"

if(a is not b) :
    print "Line 4 - a and b do not have same identity"
else :
    print "Line 4 - a and b have same identity"
