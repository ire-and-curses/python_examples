#!/usr/bin/env python

'''
car_parts.py - Simple objects for teaching aggregation.

This module holds a collection of simple classes crudely intended to represent
components of a car. Instantiations of these objects need to be plugged together
to make a working car. This is a practical demonstration of the object-oriented
concept of *aggregation* - the use of sub-objects to achieve functionality via
delegation.

Author: Eric Saunders
January 2011
'''

def print_with_stars(text):
    '''Some nice printing for in-simulation noises.'''
    print "\n", "*" * 20
    print text
    print "*" * 20, "\n"



class Wheels(object):
    '''Wheels rotate, allowing us to move across a surface.'''

    def __init__(self, car):
        self.car = car


    def rotate(self):
        headings = dict(
                         north = (0,1),
                         south = (0,-1),
                         east  = (1,0),
                         west  = (-1,0)
                        )

        pos_change = headings[self.car.heading]

        for idx in range(len(self.car.position)):
            self.car.position[idx] += pos_change[idx]

        print "The wheels rotate... you move %s." % self.car.heading


class Drivetrain(object):
    '''A Drivetrain is required to get power from the engine to the wheels.'''

    def __init__(self, wheels):
        self.wheels = wheels


    def power(self):
        self.wheels.rotate()



class SteeringWheel(object):
    '''The SteeringWheel allows direction to be changed. It also has a horn.'''

    def __init__(self):
        pass


    def steer(self, current_heading, new_direction):
        heading_mapping = {
                            'north' : {
                                        'l'  : 'west',
                                        'r'  : 'east',
                                       },
                            'east'  : {
                                        'l'  : 'north',
                                        'r'  : 'south',
                                       },
                            'south' : {
                                        'l'  : 'east',
                                        'r'  : 'west',
                                       },
                            'west'  : {
                                        'l'  : 'south',
                                        'r'  : 'north',
                                       },
                           }

        human_readable  = dict(l = 'left', r = 'right')

        new_heading     = heading_mapping[current_heading][new_direction]

        human_direction = human_readable[new_direction]
        print "Turning %s... new heading is %s." % (human_direction, new_heading)

        return new_heading


    def beep_horn(self):
        print_with_stars("BEEEEEEEEEEP!")





class Engine(object):
    '''An Engine is required to power the vehicle. It needs access to fuel, and
       a way to transmit its power.'''

    def __init__(self, petrol_tank, drivetrain):
        self.petrol_tank = petrol_tank
        self.drivetrain  = drivetrain

        self.state = "OFF"


    def toggle(self):
        if self.state == "OFF":
            self.start()
        else:
            self.stop()


    def start(self):
        if self.petrol_tank.has_petrol:
            self.state = "ON"
            print_with_stars("Brrrrm! Purr...")
            print "The engine is now running."
        else:
            print_with_stars("Aheh, click, click...")
            print "[Sounds like you need to fill the petrol tank first...]"


    def stop(self):
        self.state = "OFF"
        print "The engine shuts off."


    def increment_rpm(self):
        if self.state == "ON":
            self.drivetrain.power()
        else:
            print "You might want to try starting the engine first."



class Accelerator(object):
    '''An Accelerator is how a driver interacts with the engine.'''

    def __init__(self, engine):
        self.engine = engine


    def press(self):
        self.engine.increment_rpm()



class PetrolTank(object):
    '''A full PetrolTank is required by the engine.'''

    def __init__(self):
        self.has_petrol = False


    def fill(self):
        self.has_petrol = True
        print_with_stars("Glug glug glug...")
        print "[The petrol tank is now full]"



class Dashboard(object):
    '''The Dashboard, once hooked up, allows the engine and petrol tank internal
       states to be inspected.'''

    def __init__(self, engine, petrol_tank):
        self.engine      = engine
        self.petrol_tank = petrol_tank


    def read(self):
        text = ""
        if self.petrol_tank.has_petrol:
            text += "Petrol tank: Full\n"
        else:
            text += "Petrol tank: Empty\n"

        text += "Engine: %s." % self.engine.state

        print_with_stars(text)


class AbstractCar(object):
    '''These are the things a Car should be able to do.'''

    def __init__(self):
        pass

    def fill_petrol_tank(self):
        pass

    def turn_ignition(self):
        pass

    def read_dashboard(self):
        pass

    def accelerate(self):
        pass

    def steer(self, direction):
        pass

    def beep_horn(self):
        pass
