#!/usr/bin/env python

'''
memory_hog.py - Simple test code to run the memory profiler on.

Author: Eric Saunders
November 2010
'''

from __future__ import division
from memory_profiling import memory, resident, stacksize, print_stats

print "Initial memory footprint"
m0, r0, s0 = print_stats()

l = []


print "\nAdditional memory consumed after 10000 integer appends"
for i in range(10000):
    l.append(i)

print_stats(m0, r0, s0)
