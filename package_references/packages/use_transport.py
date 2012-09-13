#!/usr/bin/env python



print '''
          This script is stored outside the package structure.
          IT WILL WORK.
          We can find the files we need, because:
              * the Python interpreter looks for the package,
                starting in the directory where this script is located.
      '''

from vehicle.car.wheels import Wheel
from vehicle.plane.wings import Wing

wheel = Wheel()
wheel.turn()
