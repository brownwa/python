#!/usr/local/bin/python

# Sunday January 24, 2016
# tuples.py
# Waheed Brown
#
# Python Tutorial
# http://www.tutorialspoint.com/python/python_variable_types.htm

# A tuple is a READ-ONLY list, cannot be modified
tuple = ('abcd', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print tuple

try:
    tuple[3] = 1000
except Exception as e:
#    print( dir(e) ) # print all attributes of e
    print "ERROR: " + e.message
    raw_input("Press any key to continue:\n")

print tinytuple * 2
print tuple + tinytuple

