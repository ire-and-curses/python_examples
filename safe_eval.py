#!/usr/bin/env python

'''
safe_eval.py - Evaluate externally provided Python in a safe way.

Using Python as a configuration language is convenient, but the possibility of
executing arbitrary code is a serious concern. This program shows a simple way
of reading and executing Python input safely.

Only strings, numbers, tuples, lists, dicts, booleans, and None are accepted.

http://docs.python.org/library/ast.html

Author: Eric Saunders
May 2011
'''

import ast

fh = open('sample_input/to_eval.dat', 'r')

a = ast.literal_eval(fh.readline())
b = ast.literal_eval(fh.readline())

print 'a =', a
print 'b =', b

invalid = ast.literal_eval(fh.readline())
