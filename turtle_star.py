#!/usr/bin/env python

'''
turtle_star.py - Draw a star

Author: Eric Saunders
October 2011
'''

from __future__ import division
import turtle
import time

def make_atom(l):
    for i in range(20):
        turtle.fd(l)
        turtle.left(90 + 360/5)

def make_star(l):
    for i in range(5):
        turtle.fd(l)
        turtle.right(144)

def make_house(l):
    house_length = 50
    for i in range(4):
        turtle.fd(house_length)
        turtle.left(90)

    turtle.left(180)
    turtle.fd(house_length)
    turtle.right(45)
    turtle.fd(2 * house_length*house_length)



turtle.ht()

l = 200

make_atom(l)
#make_house(l)


raw_input("Press enter to close.")
