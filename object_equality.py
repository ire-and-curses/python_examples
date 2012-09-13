#!/usr/bin/env python

'''
object_equality.py - Example of generalised object equality comparisons.

It's often the case that we would like to compare objects based on the values of
their attributes. This is a particularly common problem in unit testing.

When objects are in data structures, this doesn't work because default object
comparison is by memory address. In the case of complex objects,
which may be aggregated from sub-objects, which themselves may be aggregates,
testing for equality can become a real pain.

The class below allows a child to be tested by comparing attributes between the
child and the other object. Simply inherit from this class to gain the functionality.

Type checking is included to ensure that sub-classes are identified as not-equal.
Depending on how much duck-typing you are comfortable with, this may not be what
you want.

Author: Eric Saunders
March 2012
'''

class EqualityMixin(object):
    '''Inherit from this class if you want your object to have simple equality
       properties based on common attributes (this is what you usually want).'''

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
