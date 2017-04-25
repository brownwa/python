#!/usr/local/bin/python

# Saturday January 23, 2016
# test.py
# Waheed Brown
#
# Python Tutorial
# http://www.tutorialspoint.com/python/python_command_line_arguments.htm
#
# Python (2.x) Debugging
# https://docs.python.org/2/library/pdb.html

import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    helpmsg = 'test.py -i <inputfile> -o <outputfile>'

    try:
        # getopt.getopt() returns two elements
        #
        # 1st element: opts
        # - A list of (option, value) pairs
        #   eg) for opt, arg in opts:
        #
        # 2nd element: args
        # - List of remaining arguments after the specified
        #   option list was stripped
        #
        opts, args = getopt.getopt( argv, "hi:o:", ["ifile=", "ofile="] )
    except getopt.GetoptError:
        print helpmsg
#        import pdb; pdb.set_trace(); # DEBUG
        sys.exit(2)

    # Handle no parameters
    if len(argv) <= 1:
            print helpmsg
            sys.exit(2)
    
    # Handle incorrect parameters
    for token in args:
        if token:
            print token, "is not an acceptable parameter"
            print helpmsg
            sys.exit(2)

    # Handle correct parameters
    for opt, arg in opts:
        if opt == '-h':
            print helpmsg
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        
    # NOTE: We use a series of elifs and not ifs because
    #       the for loop cycles through each (option, value)
    #       pair.

    print 'Input file is "', inputfile, '"'
    print 'Output file is "', outputfile, '"'

if __name__ == "__main__":
    main(sys.argv[1:])
    # [] and [:] are the slice operators
    # [1:] captures string starting from 2nd character
