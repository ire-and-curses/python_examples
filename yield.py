#!/usr/bin/env python

'''
yield.py - Use of the yield keyword

Author: Eric Saunders
April 2011
'''



def int_iterator(n):
    x = 0
    while x < n:
        yield x
        x += 2


for a in int_iterator(5):
    print a
