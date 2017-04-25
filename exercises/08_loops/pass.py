#!/usr/local/bin/python

# Monday April 25, 2016
# pass.py
# Waheed Brown
#
# Python Tutorial
# http://www.tutorialspoint.com/python/python_pass_statement.htm

for letter in "Python":
    if letter == 'h':
        pass # null operation, does nothing
        print "This is a pass block"
    print "Current Letter :", letter

print "Good bye!"
