#!/usr/local/bin/python

# Sunday January 24, 2016
# attributes.py
# Waheed Brown
#
# Python Tutorial
# http://www.tutorialspoint.com/python/python_variable_types.htm

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john',
            'code': 6734,
            'dept': 'sales'}

print dict['one']
print dict[2]
print tinydict

# List all the attributes of a type/variable
print dir(tinydict)
