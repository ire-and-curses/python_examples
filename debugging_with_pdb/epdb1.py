#!/usr/bin/env python

'''
epdb1.py - Experiemnting with the Python debugger.

Based on the tutorial at
http://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/

Author: Eric Saunders
April 2011
'''

import pdb

a = "aaa"

pdb.set_trace()

b = "bbb"
c = "ccc"

final = a + b + c
print final
