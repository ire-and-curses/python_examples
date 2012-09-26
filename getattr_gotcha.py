#!/usr/bin/env python

'''
getattr_gotcha.py - Unintuitive behaviour of __getattr__ - beware!

I'll fill this with the explanation in once Strawbs has had a chance
to puzzle over it...

Author: Eric Saunders
September 2012
'''


class WorkingDelegatingIterator(object):
    '''This simple class is iterable. Iteration is delegated explicitly; everything
       else is delegated via __getattr__.'''

    def __init__(self):
        self.x = [1,2,3]

    def __iter__(self):
        return self.x.__iter__()

    def __getattr__(self, attr):
        return getattr(self.x, attr)


class BrokenDelegatingIterator(object):
    '''This class quite reasonably tries to delegate everything via __getattr__.
       Some things work. So why doesn't iteration?'''

    def __init__(self):
        self.x = [1,2,3]

    def __getattr__(self, attr):
        return getattr(self.x, attr)



if __name__ == '__main__':

    print "1) Trying iterator with explicitly defined __iter__():"
    print "Getting length via __getattr__():"
    delegator = WorkingDelegatingIterator()
    print "Length:", delegator.__len__()
    print "Trying iteration:"
    for value in delegator:
        print value

    print

    print "2) Trying iterator with implicitly defined __iter__(), via __getattr__():"
    print "Getting length via __getattr__():"
    delegator = BrokenDelegatingIterator()
    print "Length:", delegator.__len__()   # This works...
    print "Trying iteration:"
    for value in delegator:                # So why doesn't this?
        print value
