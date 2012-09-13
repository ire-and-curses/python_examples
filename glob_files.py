#!/usr/bin/env python

'''
glob_files.py - Do something with all the files in a directory

Author: Eric Saunders
November 2010
'''

from glob import glob
from os.path import basename
from sys import argv

music_dir = argv[1]

for artist in glob(music_dir + '/*'):
    print 'Artist:', basename(artist)
    for album in glob(artist + '/*'):
        print '    Album:', basename(album)
