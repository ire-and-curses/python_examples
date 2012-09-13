#!/usr/bin/env python

'''
consume_pickle.py - Example of reading in a complex, pickled object.

Compare the printed output to the objects defined in make_pickle.py, the
creator of the pickled file.

Author: Eric Saunders
October 2010
'''

from __future__ import division
import pickle

pickle_filename = 'dumped_pickles.dat'
in_fh = open(pickle_filename, 'r')

complex_object1 = pickle.load(in_fh)
complex_object2 = pickle.load(in_fh)


in_fh.close()
print '\ncomplex_object1:'
print complex_object1
print '\ncomplex_object2:'
print complex_object2
