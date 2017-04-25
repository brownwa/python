#!/usr/local/bin/python

# Sunday January 24, 2016
# bitwise_operators.py
# Waheed Brown
#
# Python Tutorial - Bitwise Operators
# http://www.tutorialspoint.com/python/arithmetic_operators_example.htm
#
# XOR ^
# A B (A XOR B)
# 0 0     0
# 0 1     1
# 1 0     1
# 1 1     0
#
# Binary Ones Compliment ~
# Flips bits

a = 60    # 60 = 0011 1100
b = 13    # 13 = 0000 1101
c = 0

#"{0:016b}".format(0x1234) # unnecessary apparently
print "a =\t\t", a, format(a, '08b')
print "b =\t\t", b, format(b, '08b')
print ""

c = a & b # 12 = 0000 1100
#print "c = a & b =", c, bin(c)          # messy output
print "c = a & b =\t", c, format(c, '08b') # cleaner
                                         # 8 digit binary num
c = a | b # 61 = 0011 1101
print "c = a | b =\t", c, format(c, '08b')

c = a ^ b # XOR
          # 49 = 0011 0001
print "c = a ^ b =\t", c, format(c, '08b')

c = ~a # One's compliment (flip bits)
       # -61 = -0011 1101
print "c = ~a = \t", c, format(c, '09b')

c = a << 2; # 240 = 1111 0000
print "c = a << 2 =\t", c, format(c, '08b')

c = a >> 2; # 15 = 0000 1111
print "c = a >> 2 =\t", c, format(c, '08b')
