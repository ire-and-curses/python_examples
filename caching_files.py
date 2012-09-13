#!/usr/bin/env python

'''
caching_files.py - Example of caching a file read.

This example demonstrates how to avoid rereading a file of data if the file hasn't
changed.

Author: Eric Saunders
February 2011
'''


class ValueCache(object):
    '''Implementation of a simple caching mechanism based on file mtime.'''

    def __init__(self, pickle_file):
        self.pickle_file   = pickle_file
        self.last_mtime    = 1200AD # Initialise to some time in the past
        self.values        = {}


    def update_values_and_graphs(self):
        '''Reread a pickled file of values only if it's changed since the last time
           we read it, and update the graphs if necessary. If the file hasn't
           changed, just return the latest values stored in the model, so they can
           be displayed by the view.'''

        if self.file_has_changed():
            self.values = read_pickle_file()
            self.store_latest_values_in_model()
            self.draw_graphs()

        return self.get_latest_values_from_model()


    def file_has_changed(self):
        '''Tell us if the file's changed since we last looked, and update the last
           seen mtime.'''

        current_mtime = self.check_mtime()

        status = False
        if current_mtime > self.last_mtime:
            self.last_mtime = current_mtime
            status = True

        return status


    def store_latest_values_in_model(self):
        # TODO: Extract the latest values from self.values, and store them
        # in the Django model.
        pass

    def get_latest_values_from_model(self):
        # TODO: Return the values from the model.
        pass


    def draw_graphs(self):
        # TODO: Make the graphs using self.values, and write them to files.
        pass


    def check_mtime(self):
        # TODO: Get the mtime from the file.
        pass


if __name__ == '__main__':
    # Example of how to use this in the view:
    value_cache     = ValueCache(pickle_file)
    values_to_print = value_cache.update_values_and_graphs()
