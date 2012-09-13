#!/usr/bin/env python

'''
find_duplicate_files.py - Identify identical files, even if they have different
names.

Author: Eric Saunders
January 2011
'''

import hashlib
import os
import os.path
import sys

def create_checksum(path):
    ''' Read a file, and creates a cumulative checksum, line by line. The final
        total checksum is returned.'''

    fh = open(path)
    checksum = hashlib.md5()

    chunksize = 8192
    while True:
        buffer = fh.read(chunksize)
        if not buffer: break
        checksum.update(buffer)

    fh.close()
    checksum = checksum.digest()

    return checksum


def build_file_paths(path):
    '''Recursively traverse the filesystem, starting at path, and return a full list
       of files.'''

    path_collection = []
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath, file)
            path_collection.append(fullpath)

    return path_collection


def find_duplicates(path='.'):
    '''Determine duplicate files based on filesize, and checksum. We use a
       dictionary to avoid n*n lookup times.'''
    duplicates = []
    seen = {}

    file_list = build_file_paths(path)

    print "Traversed %d files." % len(file_list)

    for file in file_list:
        compound_key = (os.path.getsize(file), create_checksum(file))
        if compound_key in seen:
            duplicates.append(file)

        else:
            seen[compound_key] = file

    return duplicates


if __name__ == '__main__':
    # Default to the current directory
    path = '.'
    dup_log = 'duplicates.log'


    if len(sys.argv) > 1:
        path = sys.argv[1]

    print "Searching for duplicates in '%s' ..." % path

    duplicates = find_duplicates(path)

    if duplicates:
        print "Found %d duplicates." % len(duplicates)
        print "Writing duplicates to %s..." % dup_log
        dup_fh = open(dup_log, 'w')
        for dup in duplicates:
            dup_fh.write(dup + "\n")

        dup_fh.close()
        print "Done."

    else:
        print "No duplicates found."

