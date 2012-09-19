#!/usr/bin/env python
'''
memory_profiling.py - Grab memory usage stats from /proc.

Based on Python cookbook, recipe 8.2.

Author: Eric Saunders
November 2010
'''


from __future__ import division

import os

_proc_status = '/proc/%d/status' % os.getpid()
_scale = dict(
               kB = 1024.0, mB = 1024.0 * 1024.0,
               KB = 1024.0, MB = 1024.0 * 1024.0,
              )

def _VmB(VmKey):
    ''' Given a VmKey string, returns a number of bytes.'''

    # Get pseudo-file /proc/<pid>/status
    try:
        t = open(_proc_status)
        v = t.read()
        t.close()

    except IOError:
        return 0.0 # non-Linux?

    # Get VmKey line, e.g. 'VmRSS: 9999 kB\n ...'
    i = v.index(VmKey)

    # Split on runs of whitespace
    v = v[i:].split(None, 3)

    if len(v) < 3:
        return 0.0  # invalid format?

    # Convert the Vm value to bytes
    return float(v[1]) * _scale[v[2]]


def memory(since=0.0):
    ''' Returns the virtual memory usage in bytes.'''
    return _VmB('VmSize:') - since


def resident(since=0.0):
    ''' Returns the resident memory usage in bytes.'''
    return _VmB('VmRSS:') - since


def stacksize(since=0.0):
    ''' Returns the stack size in bytes.'''
    return _VmB('VmStk:') - since


def print_stats(m0=0.0, r0=0.0, s0=0.0):
    m = memory(m0)
    r = resident(r0)
    s = stacksize(s0)

    print "virtual memory (KB):", m/1024
    print "resident (KB):", r/1024
    print "stacksize (KB):", s/1024

    return m, r, s
