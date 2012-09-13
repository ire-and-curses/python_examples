#!/usr/bin/env python




print '''
          This script is stored outside the package structure.
          IT WON'T WORK.
          We can't find the files we need, because:
              * the Python interpreter looks for the package,
                starting in the directory where this script is 
                located, but the package isn't defined from here
                - it is stored in an ordinary subdirectory 
                (called packages).
      '''

from vehicle.car.wheels import Wheel
from vehicle.plane.wings import Wing


wheel = Wheel()
wheel.turn()
