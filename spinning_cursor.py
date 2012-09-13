#!/usr/bin/env python

'''
spinning_cursor.py - Implementations of command line spinners, to indicate busyness

Author: Eric Saunders
September 2012
'''
import sys
import time


def run_simple_spinner(dt):
    spin_chars = '\|/-'
    backspace = '\b'

    for i in range(5):
        for j in spin_chars:
            #print "%s%s%s" % (backspace, backspace, j),
            sys.stdout.write("%s%s" % (backspace, j))
            sys.stdout.flush()
            time.sleep(dt)


def clever_spinner():
    cursor='/-\|'
    i = 0

    while True:
        yield cursor[i]
        i = (i + 1) % len(cursor)

def run_clever_spinner(dt):
    backspace = '\b'
    for char in clever_spinner():
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(dt)
        sys.stdout.write(backspace)



print "Simple spinner:"
print "processing...  ",
#run_simple_spinner(0.2)
print '\bdone.'

print "Clever spinner:"
print "processing...  ",
run_clever_spinner(0.2)
print '\bdone.'
