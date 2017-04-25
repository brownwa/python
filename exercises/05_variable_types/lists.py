#!/usr/local/bin/python

# Sunday January 24, 2016
# lists.py
# Waheed Brown
#
# Python Tutorial
# http://www.tutorialspoint.com/python/python_variable_types.htm

list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print list
print list[0]
print list[1:3]  # 2nd to 3rd elements (2 total)

print '\n'

print list[0:-1] # 1st to 2nd last elements
print list[-1:1] # nothing
print list[-1]   # last element

print list[2:]
print tinylist * 2    # print list twice, within square brackets
print list + tinylist # concat, within square brackets
