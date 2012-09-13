#!/usr/bin/env python

'''
polymorphic_output.py - Use polymorphic objects to save program state.

In this exercise, you will be implementing a system for recording fascinating facts
about your friends. The code will be able to read and write to several different
kinds of output systems, to allow your information to be retained between multiple
runs of your program.

Copy this file to your workspace and fill in the blanks. :)

Author: Eric Saunders
April 2011
'''

# 0) Ask the user for a file to read. Determine how to read it based on extension:
    # .txt
    # .pickle
    # .json

# 1) Read in information in any of the supported formats (or none)
    # As a plain text file
    # As a pickle
    # As JSON


# 2) Using an InteractiveReadWriter object, print the information we have


# 3) Using an InteractiveReadWriter object, Ask the user to input some information
# about their friends:
    # First name
    # Last name
    # Personality traits (any number of traits, separated by commas)
    # Additional notes (a sentence)


# Write out the information in a choice of several formats:
    # As a plain text file
    # As a pickle
    # As JSON



# Create a reader/writer object for each serialisation method (including
# printing to screen!). These objects should
# be polymorphic, with the following method signatures:

class ReadWriter(object):

    def __init__(self, infile=None, outfile=None):
        self.infile  = infile
        self.outfile = outfile


    def read(self):
        # Example steps (these will vary between each object):
        # Open the file
        # Read the file contents
        # Convert the data into a common programmatic form (e.g. list of dicts)
        # Close the file
        # Return the data
        pass

    def write(self):
        # Open the file
        # Write the data
        # Close the file
        pass


# EXTRA CREDIT: Add a fourth serialisation mechanism - Berkely DB. See recipe 7.8
# in the Python Cookbook, 2nd edition. If you can do this, you will have reached
# a good understanding of polymorphism! :)
