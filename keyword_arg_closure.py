#!/usr/bin/env python
# Basic example of closures in python

# The general function
def a(keyword_arg1='Eric', keyword_arg2='Orange'):
    print keyword_arg1, keyword_arg2

# The closure
def outer(new_colour='Purple'):
    return a(keyword_arg1='Tim', keyword_arg2=new_colour)

# The closure being executed
def function_executor(func_to_run):
    func_to_run()



function_executor(outer)

