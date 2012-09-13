#!/usr/bin/env python

'''
regex_tester.py - Interactively test a regex for matching properties.

Author: Eric Saunders
December 2010
'''


import re

#regex = r'.*your face(?P<num>\d+)'
#regex = r'^DataOut/(?P<site>\w{3})/(?P<timeInterval>\d+)/(?P<key>[a-z_.]+)/$'
#regex = r'.*href=(\d+\.log)'
#regex = r'^telemetry/find /(?P<site>[a-zA-Z_0-9]+)/$'

#regex = r'log_bfin_mres[a-zA-Z_0-9]+.txt$'
regex  = r'[\d]{1,3}$'

print "Regex: '%s'" % regex

pattern = re.compile(regex, re.IGNORECASE)


while (True):
    string = raw_input('>')
    match  = re.match(pattern, string)
    #matches = re.findall(pattern, string)

    if match:
        print "Matched"
        print "Unnamed groups:", match.groups()
        print "Named groups:", match.groupdict()

    else:
        print "No match."
