#!/usr/bin/env python

'''
small_plot.py - Make a plot with a small size

Author: Eric Saunders
December 2010
'''

from math import pi
from numpy import arange, sin
import matplotlib.pyplot as mp


t = arange(0.0, 2.0, 0.01)
s = sin(2*pi*t)
my_dpi = 10

# Inches x dpi = pixels
# 4 x 4 * 50dpi = 200x200 pixels
# Defaults: figsize = (8,6), dpi=80 => 640x480
fig = mp.figure(figsize=(19,5), dpi=my_dpi)
mp.plot(t, s, linewidth=1.0)

mp.xlabel('time (s)')
mp.ylabel('voltage (mV)')
mp.title('How your intelligence varies with time')
mp.legend(['Your face'], loc=(1.01, 0.75))
mp.grid(True)
#mp.show()
mp.savefig('your_face.png', dpi=my_dpi)
