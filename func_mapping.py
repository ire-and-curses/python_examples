#!/usr/bin/python


class Angle(object):

    def __init__(self, **kwargs):

        self.unit_mapping = {
                                'degrees'     : self.from_degrees,
                                'radians'     : self.from_radians,
                             }        
        
        try:
            for key in kwargs:
                self.degrees = self.unit_mapping[key](kwargs[key])
        except KeyError as e:
            msg = ("Error constructing Angle: " + str(e)
                  + " is not a valid unit. Try 'degrees' or 'radians' instead.")

            print msg
            raise

    def from_degrees(self, degrees):
        self.degrees = degrees
        print 'Set from_degrees'
        
        
    def from_radians(self, radians):
        self.degrees = degrees(radians)




angle = Angle(eggs = 90)
