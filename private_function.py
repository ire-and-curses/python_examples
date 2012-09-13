#!/usr/bin/env python

'''
private_function.py - Hilarious example of private function implementation.

Based on an example here:

http://stackoverflow.com/questions/70528/why-are-pythons-private-methods-not-actually-private

Author: Eric Saunders
May 2012
'''

import re
import inspect

class NoPaparrazi(object):

    def __init__(self):
        pass

    def private_function(self):
        '''The private function may not be called by callers who aren't me.'''

        try :
            function_call = inspect.stack()[1][4][0].strip()

            # See if the function_call has "self." in the begining
            matched = re.match( '^self\.', function_call )
            if not matched :
                print 'This is a private function, go away.'
                return
        except :
            print 'This is a private function, go away.'
            return

        # This is the real Function, only accessible inside class #
        print 'Hey, welcome to function!'

    def public_function ( self ) :
        '''I can call the private function from inside the class.'''
        self.private_function()


if __name__ == '__main__':

    celebrity = NoPaparrazi()
    celebrity.private_function()
    celebrity.public_function()
