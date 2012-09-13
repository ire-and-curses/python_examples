#!/usr/bin/env python

'''
epdb2.py - Experimenting with the Python debugger - subroutines

Based on the tutorial at
http://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/

Author: Eric Saunders
April 2011
'''

import pdb


def combine(s1, s2):
    s3 = s1 + s2 + s1
    s3 = '"' + s3 + '"'

    return s3


a = "aaa"
pdb.set_trace()

b = "bbb"
c = "ccc"

final = combine(a,b)
print final
