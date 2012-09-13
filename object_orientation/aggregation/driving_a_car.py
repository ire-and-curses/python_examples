#!/usr/bin/env python

'''
driving_a_car.py - Implementation of a car and a simple world to drive around in.

This script implements a car via aggregation, using the car_parts library. A simple
world is provided to allow the car to be driven around.

Author: Eric Saunders
January 2011
'''


from car_parts import *
import sys

class World(object):

    def __init__(self):
        self.car = Car()


    def prompt_action(self):
        '''Execute a user-specified action.'''
        actions = (
                    ("Fill petrol tank"   , self.car.fill_petrol_tank),
                    ("Start the car"      , self.car.turn_ignition),
                    ("Read the dashboard" , self.car.read_dashboard),
                    ("Accelerate"         , self.car.accelerate),
                    ("Steer"              , self.steer),
                    ("Beep horn"          , self.car.beep_horn),
                  )


        print "Choose an action:"
        option_number = 1
        for action in actions:
            print "    %d) %s" % (option_number, action[0])
            option_number += 1

        choice = int(raw_input("> "))

        # Execute the action
        actions[choice-1][1]()


    def steer(self):

        choice = raw_input("Left (l) or right (r)? > ")
        self.car.steer(choice)


    def print_car_position(self):
        print "Your car is currently at %s." % self.car.position

        # Construct the surface
        surface = []
        width = 20
        for i in range(int(width/2)):
            surface.append("." * width)

        # Place the car on the surface
        car_sprite_mapping = dict(
                                   north = "^",
                                   east  = ">",
                                   south = "V",
                                   west  = "<"
                                  )

        origin = (int(width/2), int(width/4))
        x_position = (origin[0] + self.car.position[0])
        y_position = (origin[1] - self.car.position[1])

        # Check for the edges of the map
        if ( (x_position > width) or (x_position < 1)
             or (y_position > len(surface)-1) or y_position < 0):

            print_with_stars("CRASH!!!")
            print "Looks like you hit the edge of the world. Goodbye!"
            sys.exit()


        # Insert the car on the surface
        new_line = ("." * (x_position-1) + car_sprite_mapping[self.car.heading]
                    + "." * (width-x_position))

        surface[y_position] = new_line


        for line in surface:
            print line



class Car(AbstractCar):

    def __init__(self):
        self.heading = "north"
        self.position = [0,0]

        self.construct_components()


    def construct_components(self):
        self.steering_wheel = SteeringWheel()
        self.petrol_tank    = PetrolTank()
        self.wheels         = Wheels(self)
        self.drivetrain     = Drivetrain(self.wheels)
        self.engine         = Engine(self.petrol_tank, self.drivetrain)
        self.accelerator    = Accelerator(self.engine)
        self.dashboard      = Dashboard(self.engine, self.petrol_tank)


    def fill_petrol_tank(self):
        self.petrol_tank.fill()


    def turn_ignition(self):
        self.engine.toggle()


    def read_dashboard(self):
        self.dashboard.read()


    def accelerate(self):
        self.accelerator.press()


    def steer(self, new_direction):
        self.heading = self.steering_wheel.steer(self.heading, new_direction)


    def beep_horn(self):
        self.steering_wheel.beep_horn()


if __name__ == "__main__":
    world = World()

    while (True):
        world.prompt_action()
        world.print_car_position()
