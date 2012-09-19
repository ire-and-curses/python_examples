#!/usr/bin/env python

'''
run_for_a_while.py - Simple code for running a cpu profiler against.

Author: Eric Saunders
November 2010
'''


def func1():
    l = []
    for i in range(100000):
        l.append(i * i)

    return l

def main():
    for j in range(50):
        l = func1()

    print "Final value:", l[-1]


main()
