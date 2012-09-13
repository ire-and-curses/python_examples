#!/usr/bin/env python

'''
iterating_over_seqs.py - Examples of iterating over sequences.

Author: Eric Saunders
October 2010
'''

people = ('eric', 'strawbs', 'tim', 'zach', 'michelle')


print "3 different ways to get the index, and the value."
print "\nMethod 1"
for i in range(len(people)):
    person = people[i]
    print i, person


print "\nMethod 2"
j = 0
for person in people:
    print j, person
    j += 1


print "\nMethod 3"
for k, person in enumerate(people):
    print k, person
