#!/usr/local/bin/python

# Monday April 25, 2016
# numbers.py
# Waheed Brown
#
# Python Tutorial
# http://www.tutorialspoint.com/python/python_numbers.htm

a = 2 + 3j
b = 4 + 5j

print "a =", a
print "b =", b
print "a * b =", a * b 

c = 0x100
d = 0xF0

# ^ is XOR
print "\nc =", format(c, '#2x')
print "d = ", format(d, '#2x')
print "c ^ d", format(c ^ d, '016b') # binary
print "c ^ d", format(c ^ d, '#2x') # hexadecimal (at least 2 digits)
