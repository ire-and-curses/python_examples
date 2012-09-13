#!/usr/bin/env python

'''
type_check_args.py - Test a string for possible interpretation as an int or float

Author: Eric Saunders
October 2011
'''

import sys

def cast_string(incoming):

    try:
        cast_value = int(incoming)
        print "Type determined: '%s' is an int" % incoming
        return cast_value
    except ValueError:
        print "'%s' isn't an int..." % incoming

    try:
        cast_value = float(incoming)
        print "Type determined: '%s' is a float" % incoming
        return cast_value
    except ValueError:
        print "'%s' isn't a float..." % incoming


    print "Leaving '%s' as a string..." % incoming
    cast_value = incoming
    return cast_value



if len(sys.argv) == 1:
    print "Usage: python %s arg_to_cast" % sys.argv[0]
    exit()
incoming = sys.argv[1]

print "Got '%s'" % incoming

cast_value = cast_string(incoming)


