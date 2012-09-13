#!/usr/bin/env python

'''
polymorphism.py - Example of polymorphic classes

Author: Eric Saunders
September 2010
'''

class Animal(object):
    """Generic parent class"""
    def __init__(self, name):
        self.name = name

    def make_noise(self):
        """Default noise to make"""
        noise = 'wibbles'

        return noise


class Lion(Animal):
    def  __init__(self, name):
        Animal.__init__(self, name)

    def make_noise(self):
        noise = 'roars'

        return noise


class Mouse(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.cheese = 'Untouched'

    def make_noise(self):
        noise = 'squeaks'

        return noise

    # Even though this is a unique method to the Mouse, the class can still be
    # used polymorphically if this method is not called.
    def eat_cheese(self):
        self.cheese = 'Eaten'


class Grasshopper(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def make_noise(self):
        noise = 'chirps'

        return noise


class TimListerTheHuman(object):
    def __init__(self, name):
        self.name = name

    def cry_out_in_rage(self):
        angry_cry = 'says "Oh piss off! What is going on with this *now*?"'

        return angry_cry


class Werewolf(Animal):
    '''This is an adaptor class, making the adapted class appear to be an
       Animal.'''
    def __init__(self, name):
        self.name = name
        self.human_tim = TimListerTheHuman(name)

    def make_noise(self):
        noise = self.human_tim.cry_out_in_rage()

        return noise


if __name__ == '__main__':

    animals = (
               Lion('Simba'),
               Mouse('Mickey'),
               Grasshopper('Jiminey Cricket'),
               Werewolf('Tim Lister')
              )

    # Polymorphism: All the animals can be called in the same way.
    for creature in animals:
        print creature.name, creature.make_noise() + '.'
