#!/opt/debugpython/bin/python
##!/usr/local/bin/python

# Monday April 25, 2016
# valgrind.py
# Waheed Brown
#
# Python Tutorial
# http://www.tutorialspoint.com/python/python_numbers.htm
#
# References
# https://code.google.com/archive/p/distnumpy/wikis/valgrind.wiki

import random

# for choice(), parameter must be at least the empty set, with
# a single value of 'None' (Python null value)
print "choice( [2, 4, 6, 8] ) =", random.choice( [2, 4, 6, 8 ])
print "choice( [None] ) =", random.choice( [None] )
print "choice('A String') = ", random.choice( 'A String' )

# Select an even number in from [100, 999], inclusive
print "\nrandrange(100, 1000, 2) = ", random.randrange(100, 1000, 2)

# consistently generate the same random number using seed()
# if seed not set then system time used by default
mySeed = 10
random.seed(10)
print "Random number with seed %d = %f" % ( mySeed, random.random() )

del mySeed # freeing memory, number datatypes are immutable remember
mySeed = 11
print "Random nubmer with seed %d = %f" % ( mySeed, random.random() )
