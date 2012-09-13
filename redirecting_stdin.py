#!/usr/bin/env python

'''
redirecting_stdin.py - Set stdin to a file

Author: Eric Saunders
September 2012
'''
import sys

fh = open('sample_stdin.txt', 'r')
sys.stdin = fh

line1 = raw_input('foo: ')
line2 = raw_input('bar: ')

print line1
print line2
