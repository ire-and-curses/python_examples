#!/usr/bin/env python

'''
cmd_line_args_2.6.py - Example of using optparse for command-line arguments

Note that this is deprecated in 2.7 in favour or argparse, a suspiciously similar
library.

Example calls:
    python cmd_line_args_2.6.py --file=your_face
    python cmd_line_args_2.6.py --file=your_face -q
    python cmd_line_args_2.6.py --booboo=your_face

Author: Eric Saunders
March 2012
'''

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write report to FILE", metavar="FILE")
parser.add_option("-q", "--quiet",
                  action="store_false", dest="verbose", default=True,
                  help="don't print status messages to stdout")

(options, args) = parser.parse_args()

print "Filename:", options.filename
print "Verbosity:", options.verbose

