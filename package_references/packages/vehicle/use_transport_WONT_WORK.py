#!/usr/bin/env python




print '''
          This script is stored outside the package structure.
          IT WON'T WORK.
          We can't find the files we need, because:
              * the Python interpreter looks for the package,
                starting in the directory where this script is 
                located, but we are already inside the top-level package,
                ('vehicle'), so our name resolution fails.
      '''

from vehicle.car.wheels import Wheel
from vehicle.plane.wings import Wing


wheel = Wheel()
wheel.turn()
