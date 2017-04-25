#!/usr/local/bin/python

# Saturday December 17, 2016
# add_attributes.py
# Waheed Brown
#
# Python Advanced Tutorial: Classes/Objects
#
# Example 1:
# You can add, remove or modify class attributes dynamically
#
# Reference:
# https://www.tutorialspoint.com/python/python_classes_objects.htm

import sys

# Emplee.__doc__ to access class documentation
class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

def main(argv):
    emp1 = Employee("Jamal Gonzalez", 50000)
    emp1.age = 7
    emp1.age = 8
    del emp1.age

if __name__ == "__main__":
    main(sys.argv[1:])
    # [] and [:] are the slice operators
    # [1:] captures string starting from 2nd character
