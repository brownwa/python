#!/usr/local/bin/python

# Sunday January 24, 2016
# logical_operators.py
# Waheed Brown
#
# Python Tutorial
# http://www.tutorialspoint.com/python/logical_operators_example.htm

name01 = "Smythe"
name02 = ""

print "name01 =", name01
print "name02 =", name02

print (name01 and name02)
print (name01 or name02)
print not(name01 and name02) # prints True
print not(True) # prints False
