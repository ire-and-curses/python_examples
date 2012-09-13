#!/usr/bin/env python

'''
polymorphic_tests.py - Example of removing multiple variable if statements using
                       polymorphism.

This code answers the following Stack Overflow question:
http://stackoverflow.com/questions/5034443/looking-for-a-testing-pattern-approach-capable-of-handling-different-platforms-ve

Author: Eric Saunders
February 2011
'''

class platform_a(object):

    def __init__(self, version):
        self.version = version
        self.bla_mapping = {
                             '1.4' : 'bla',
                             '1.5' : 'ble',
                             '1.6' : 'blu'
                            }

        self.bla = self.bla_mapping[self.version]

# Dummy stubs to demo the test code
class platform_b(object):
    def __init__(self):
        # Obviously, add all platform B specific details here - this is
        # just an example stub
        self.bla = 'blu'

class platform_c(object):
    def __init__(self):
        # Obviously, add all platform C specific details here - this is
        # just an example stub
        self.bla = 'boo'

def get_the_platform(): return 'a'
def get_the_version():  return '1.4'
def result_of_running_the_real_code(): return 'bla'

def test1(platform, version):

    # Map platform names to our polymorphic platform objects
    env_mapping = dict(
                        a = platform_a,
                        b = platform_b,
                        c = platform_c,
                                       )

    # Instantiate an object corresponding to the unique environment under test
    environment = env_mapping[platform](version)

    # Get the result of running the real code in this environment
    bla = result_of_running_the_real_code()

    # Test we got what we expected
    assert(environment.bla, bla)



# The environment is presumably specified by the test harness
platform = get_the_platform()
version  = get_the_version()

# Run the test
test1(platform, version)
