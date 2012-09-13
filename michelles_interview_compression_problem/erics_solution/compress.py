#!/usr/bin/env python

'''
compress.py - summary line

description

Author: Eric Saunders
July 2012
'''

def is_valid(input_string):
    ''' A valid input consists of one or more upper case English letters A-Z. '''

    # Note that isalpha() is locale dependent.
    if input_string.isupper() and input_string.isalpha():
        return True

    return False


def write_compressed_substring(compressed, repeats):
    compressed = compressed + compressed[-1]
    compressed = compressed + str(repeats)

    return compressed


def compress(input_string):

    #~ if not is_valid(input_string):
        #~ msg = "Invalid input: input must match [A-Z]+"
        #~ raise InvalidInputError(msg)


    i = 0
    compressed = ''
    repeats    = -1
    while i < len(input_string):
        current_char = input_string[i]

        # If the buffer is empty, set it...
        if not compressed:
            compressed = current_char

        # The buffer isn't empty, so compare it with the current character...
        else:
            # If we see the same character as the last one, we've got a repeat...
            if current_char == compressed[-1]:
                repeats += 1

                # If we've reached 9 repeats, we need write this, and start again...
                if repeats == 9:
                    compressed = write_compressed_substring(compressed, repeats)
                    repeats = -1

            # Otherwise, decide how much compression happened, and write
            else:
                if repeats > -1:
                    compressed = write_compressed_substring(compressed, repeats)
                    repeats = -1

                compressed = compressed + current_char

        i += 1

    # Deal with the case of the end of the string, and repeats outstanding
    if repeats > -1:
        compressed = write_compressed_substring(compressed, repeats)


    return compressed



class InvalidInputError(Exception):
    '''Raised if the input string does not obey validation requirements.'''

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value
