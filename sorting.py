#!/usr/bin/env python

'''
sorting.py - Sorting a list of dictionaries using a value of that dictionary

Author: Eric Saunders
September 2012
'''

from operator import itemgetter

a = dict(first = 'joe', last = 'smith')
b = dict(first = 'bob', last = 'jones')

people = [a, b]

sorted_people = sorted(people, key=itemgetter('first'))
