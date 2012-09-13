#!/usr/bin/env python

'''
spiral_motion.py - Example of discretised spiral motion

Author: Eric Saunders
October 2011
'''

import turtle
turtle.shape("turtle")

def move_unit_length(pos, direction):

    direction_mapping = dict (
                               w = (-1,0),
                               n = (0,1),
                               e = (1,0),
                               s = (0,-1)
                              )

    new_pos_x = pos[0] + direction_mapping[direction][0]
    new_pos_y = pos[1] + direction_mapping[direction][1]

    return new_pos_x, new_pos_y


def move_across_side(pos, cur_direction, length):
    for i in range(1, length+1):
        pos = move_unit_length(pos, cur_direction)
        print pos

    return pos


rh_turn = dict(
                w = 'n',
                n = 'e',
                e = 's',
                s = 'w'
               )

origin        = (0,0)
n_turns       = 9
cur_direction = 'w'

print "Starting position:", origin
print "Starting direction:", cur_direction

length = 1
pos    = origin
for i in range(n_turns):

    for j in range(2):
        pos = move_across_side(pos, cur_direction, length)
        turtle_pos = (pos[0]*50, pos[1]*50)
        turtle.setpos(turtle_pos)
        cur_direction = rh_turn[cur_direction]
        turtle.right(90)

    # Increment the length
    length += 1


print "Final position:", pos
import time
time.sleep(5)
