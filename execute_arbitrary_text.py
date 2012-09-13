#!/usr/bin/env python

'''
execute_arbitrary_text.py - Read in text, and execute the string as Python.

Note that there also exists the function execfile() which does this for you.
However this approach is handy if you want to pass the content around, e.g.
over a socket.

Note that in general, use of generic exec() like this is a dangerous security
hole! Don't do it without very careful thought!

Author: Eric Saunders
November 2010
'''

def exec_file(python_filename):
    python_to_execute_fh = open(python_filename, 'r')
    code_lines = python_to_execute_fh.readlines()
    python_to_execute_fh.close()

    # Combine the list into a single long string for eval
    code = ''.join(code_lines)
    exec(code)


exec_file('../python_examples/glob_files.py')
