#!/usr/bin/env python
'''
read_config_file.py - example use of the ConfigParser library module

Author: Eric Saunders
July 2010
'''


import ConfigParser

config = ConfigParser.SafeConfigParser()
config.read('example.cfg')

my_dir = config.get('My Section', 'dir')
wotsit = config.get('My Section', 'wotsit')
weird = config.get('My Section', 'weird_val')
list = config.get('My Section', 'list')

print 'my_dir =', my_dir
print 'wotsit =', wotsit
print 'weird =', weird

for i in list:
    print i
