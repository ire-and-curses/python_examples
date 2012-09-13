#!/usr/bin/env python

'''
web2file.py - Grab a webpage and save it to a file.

Author: Eric Saunders
October 2010
'''
import urllib2
import sys

# Give up unless we got a command-line argument
if len(sys.argv) < 2:
    print "Usage: python %s url" % sys.argv[0]
    exit()

# Assume the command line argument is a url
url = sys.argv[1]

# Get a handle on the webpage
webpage = urllib2.urlopen(url)

# Save the webpage locally with the same name
out_filename = url.split('/')[-1]
out_fh = open(out_filename, 'w')

for line in webpage:
    out_fh.write(line)
out_fh.close()

print "Saved contents of %s locally as %s." % (url, out_filename)
