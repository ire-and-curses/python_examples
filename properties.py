#!/usr/bin/python

'''
properties.py - Example of using the property function to provide getters/setters

Properties behave like instance variables, but access is through methods.
Note that this only works with new-style classes.

See extended discussion at
http://www.python.org/download/releases/2.2.3/descrintro/

Author: Eric Saunders
December 2009
'''


class prop(object):

    def __init__(self):
        self.__x = 0

    # You must use a dummy variable, such as self._x
    # If you did e.g. return self.x then that would recurse and call def get_x()
    # again... -> infinite recursion!
    def get_x(self):
        return self.__x

    def set_x(self, x):
        if x < 0: x = 0
        self.__x = x


    def get_pi(self):
        return 3.14159

    # In general, don't bother setting this for constants - will then raise an
    # AttributeError when called.
    def set_pi(self, value):
        print "You can't change PI! Geometry forbids it!"

    x  = property(get_x, set_x)
    pi = property(get_pi, set_pi, doc="Returns the value of pi")




# Usage with standard getter/setter
print "Usage with standard getter/setter"
print "---------------------------------"
instance = prop()
instance.x = 10
print instance.x

instance.x = -10
print instance.x

instance.set_x(12)
print instance.get_x()
print

# Pi examples
print "Pi examples"
print "-----------"
print "1", instance.pi
print "2", prop.pi.__doc__

# This won't work
instance.pi = 17
print instance.pi

print prop.pi
