#!/usr/local/bin/python

# Monday April 25, 2016
# while_nested.py
# Waheed Brown
#
# Python Tutorial
# http://www.tutorialspoint.com/python/python_nested_loops.htm

i = 2
while(i < 100):
    j = 2
    while(j <= (i / j) ):
        if not(i % j): break # if j is a factor of i then next i
        j = j + 1
    if(j > (i / j) ): print i, "is a prime"
    i = i + 1

print "Good bye!"