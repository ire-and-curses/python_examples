#!/usr/bin/env python

'''
make_pickle.py - Example of creating pickled objects.

Author: Eric Saunders
October 2010
'''

from __future__ import division
import pickle

complex_object1 = {
                    'one' : [1,2,3],
                    'two' : ("bacon and pesto tagliatelle", "for whom the bell tolls"),
                    'three' : ("twas brillig", 53, { 'your_face' : 'dumb' } ),
                    'four' : {'a' : 1, 'second' : 2, 'dictionary' : 3},
                   }


complex_object2 = (
                    [4,5,6],
                    ("depends on what you mean", "it tolls for thee"),
                    ( {'I see' : 'that'}, 5.456, { 'your_face' : 'dumb' } ),
                    {'a' : 1, 'second' : 2, 'dictionary' : 3},
                   )

pickle_filename = 'dumped_pickles.dat'
out_fh = open(pickle_filename, 'w')

pickle.dump(complex_object1, out_fh)
pickle.dump(complex_object2, out_fh)

out_fh.close()

print "Wrote out pickle file as '%s'." % pickle_filename
