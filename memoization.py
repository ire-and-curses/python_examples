#!/usr/bin/env python

'''
memoization.py - Transparent memoization using decorators.

Author: Eric Saunders
January 2011
'''


class Memoize(object):

    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        print "Args:", args

        if not args in self.cache:
            print "...not found..."
            answer = self.func(*args)
            print "Added", answer, "to cache..."
            self.cache[args] = answer

        return self.cache[args]

    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__


class SimpleDecorator(object):

    def __init__(self, f):
        print "Inside SimpleDecorator constructor."
        self.f = f

    def __call__(self):
        print "Inside SimpleDecorator call"
        self.f()
        print "Finished executing function"


@Memoize
def fibonacci(n):
    if n in (0, 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def decorate(f):
    def decorated():
        print "Decorating..."
        f()
        print "Finished decorating."

    return decorated


indent = "   "
#@decorate
def hello_world():
    global indent
    
    print "Hello, world!"
    print indent, "blah"

    indent = "      "
    #recurse
    indent = "   "

#f = Memoize(fibonacci)
#g = SimpleDecorator(hello_world)
#h = decorate(hello_world)

print fibonacci(10)
print fibonacci(110)
#print f(12)
#g()
#h()
#hello_world()
