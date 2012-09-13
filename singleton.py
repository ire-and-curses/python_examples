#!/usr/bin/env python

def singleton(object, instantiated=[]):
    "Raise an exception if an object of this class has been instantiated before."
    
    print instantiated

    assert object.__class__ not in instantiated, \
        "%s is a Singleton class but is already instantiated" % object.__class__
    
    instantiated.append(object.__class__)


class YourClass:
    "A singleton class to do something ..."
    def __init__(self):
        singleton(self)        

    def test(self, egg=[]):
        print egg
        egg.append('your face')
        


a = YourClass()
a.test()
a.test()
a.test()
a.test()
a.test()


a = YourClass()

