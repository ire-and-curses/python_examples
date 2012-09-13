#!/usr/bin/env python

'''
profile_code.py - Example of profiling CPU usage.

See: http://docs.python.org/library/profile.html

Author: Eric Saunders
November 2010
'''

# To run a simple profile from the command line:
# python -m cProfile run_for_a_while.py 
# Ordered by time:
# python -m cProfile -s time run_for_a_while.py



from run_for_a_while import main

import cProfile
import pstats

#cProfile.run('main()', 'run.prof')



p = pstats.Stats('run.prof')

# Print the 10 most significant lines, by cumulative time
#p.sort_stats('cumulative').print_stats(10)

# Print the functions that take the most time
p.sort_stats('time').print_stats(30)

