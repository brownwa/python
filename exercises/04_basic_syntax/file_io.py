#!/usr/local/bin/python

# Saturday January 23, 2016
# file_io.py
# Waheed Brown
#
# Python Tutorial
# http://www.tutorialspoint.com/python/python_basic_syntax.htm

import sys

# enter file name
file_name = raw_input("Enter file name: ")
file_finish = "EOF"

try:
    # open file stream
    file = open(file_name, "w")
except IOError:
    print "There was an error writing to ", file_name
    sys.exit()

print "Enter '", file_finish, "' when finished"

file_text = ""
while file_text != file_finish:
    file_text = raw_input("Enter text: ")

    if file_text == file_finish:
        # close the file
        file.close
        break

    file.write(file_text)
    file.write("\n")

file.close()

if len(file_name) == 0:
    print "Next time please enter something"
    sys.exit()

file = open(file_name, "r")
read_text = file.read()
file.close()
print read_text
