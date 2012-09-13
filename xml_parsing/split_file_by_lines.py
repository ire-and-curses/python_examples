#!/usr/bin/env python

'''
split_file_by_lines.py - Chop a file up into many files, one per line

This little tool is for splitting an XML dump from a DB into individual documents,
for reading by a SAX parser.

Author: Eric Saunders
May 2012
'''

import sys


if len(sys.argv) > 1:
    dump_file_to_read = sys.argv[1]



dump_fh = open(dump_file_to_read, 'r')

for n, line in enumerate(dump_fh):
    out_file = "dump_file_to_read_%s" % n
    out_fh   = open(out_file, 'w')
    out_fh.write(line)
    out_fh.close()

dump_fh.close()
