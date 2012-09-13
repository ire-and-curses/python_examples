#!/usr/bin/env python

'''
decorate.py - Examples of decorators and closures.

description

Author: Eric Saunders
April 2011
'''


def add_waffle(f):

    def waffler():
        print "Waffle waffle"
        f()
        print "Finished waffling"

    return waffler



@add_waffle
def hello_world():
    print "Hello, world!"



#decorated_stuff = add_waffle(hello_world, "cheese")

#decorated_stuff2 = add_waffle(hello_world, "pastrami")

#decorated_stuff()
#decorated_stuff2()

#decorated_stuff3 = add_waffle(decorated_stuff2, "mushrooms")
#decorated_stuff3()


hello_world()
