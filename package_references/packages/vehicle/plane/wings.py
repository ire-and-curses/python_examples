#!/usr/bin/env python

# This import statement works, because we are doing an import, not running a script.
# Python has special behaviour where it searches the package hierarchy that this module
# is a part of, to look for the module you are trying to import.

from vehicle.car.wheels import Wheel

class Wing(object):

    def __init__(self):
        self.wheel = Wheel()

    def lift_ailerons(self):
        pass

    def land_plane(self):
        self.wheel.turn()
