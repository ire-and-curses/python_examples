'''
flatten_lists.py - Combine two nested lists of tuples, using itertools

Example of how to use itertools to combine two lists of the form
( (a, b), (c, d) ) to produce a single flattened list of all the elements

Author: Eric Saunders
November 2011
'''

from itertools import chain


a = ( (3, 4), (2, 1) )
b = ( (5, 6), (7, 8) )


flat_iterator = chain(chain.from_iterable(a), chain.from_iterable(b))


# If all you want is to go through the elements, use the flat iterator. If you need
# e.g. to sort the values, then you need to dump to a list first.

flat_list = list(flat_iterator)
flat_list.sort()

for i in flat_list:
    print i
