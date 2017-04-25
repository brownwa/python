#!/usr/local/bin/python

# Saturday February 6, 2016
# trace.py
# Waheed Brown
#
# Python Tutorial
# http://www.tutorialspoint.com/python/python_for_loop.htm

import pdb; pdb.set_trace() # TESTING LINE

for num in range(10, 20) :    # iterate from 10 to 20
    for i in range(2, num) :  # iteratre from 2 to num
        if( (num % i) == 0) : # if i is a factor of num
            j = num / i

