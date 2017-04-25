#!/usr/local/bin/python

# Saturday December 17, 2016
# builtin_attr.py
# Waheed Brown
#
# Python Advanced Tutorial: Classes/Objects
#
# Reference:
# https://www.tutorialspoint.com/python/python_classes_objects.htm

import sys

class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name: ", self.name, ", Salary: ", self.salary

def main(argv):
    print "Employee.__doc__", Employee.__doc__
    print "Employee.__name__", Employee.__name__
    print "Employee.__module__", Employee.__module__
    print "Employee.__bases__", Employee.__bases__
    print "Employee.__dict__", Employee.__dict__

if __name__ == "__main__":
    main(sys.argv[1:])
    # [] and [:] are the slice operators
    # [1:] captures string starting from 2nd character
