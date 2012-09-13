#!/usr/bin/env python

'''
set_intersections.py - Examples of sets in action

Author: Eric Saunders
September 2012
'''

a = set([1, 2, 3, 4, 5])
b = set([2, 5, 6])

# Set membership
if 2 in a:
    print True


# The union (members of either a OR b)
union = a | b

# The intersection (members of both a AND b)
intersection = a & b

# The complement (members in one set but not the other)
complement = a - b

print 'Union:', union
print 'Intersection:', intersection
print 'Complement:', complement
