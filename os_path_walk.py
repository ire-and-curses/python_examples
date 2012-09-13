#!/usr/bin/python

'''
os_path_walk.py - example of how to use the os.path.walk function

description

Author: Eric Saunders
July 2009
'''

import os.path
import re


def match_fits_files(arg, dirname, names):
    '''Executed by os.path.walk for each directory recursively traversed.'''

    print "Entered directory '%s'" % dirname

    for filename in names:
        (basename, suffix) = os.path.splitext(filename)

        # Match files that end '.dif.fits'
        file_is_fits = re.search(r'\.dif\.fits$', filename, re.IGNORECASE)

        if not file_is_fits:
            continue

        # Do your arbitrary action here
        print "****Found matching file:", filename, "****"


print "Starting traverse..."
# You can pass in your own arguments here using this variable
arg = ''

# The root of the directory path you want to traverse
path = '.'

os.path.walk(path, match_fits_files, arg)

