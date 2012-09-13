#!/usr/bin/env python
'''
logplot.py - Plot a graph with log axes using matplotlib.

Author: Eric Saunders
September 2010
'''

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)

s = np.sin(2*np.pi*t)
#plt.plot(t, s, linewidth=1.0)
plt.semilogx(t, s, 'r+', linewidth=1.0, basex=10)
plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.show()
plt.savefig('crap.png')
