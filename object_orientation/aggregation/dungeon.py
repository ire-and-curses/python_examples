#!/usr/bin/env python

'''
dungeon.py - Components for a basic dungeon adventure game.

Author: Eric Saunders
February 2011
'''

import os


class Game(object):

    def __init__(self, dungeon):
        self.dungeon = dungeon

    def run_game_loop(self):

        self.dungeon.enter()

        while True:
            action = raw_input('> ')

            if action == 'look':
                self.dungeon.hero.look()

            elif ( action == 'north' or action == 'south'
                    or action == 'east' or action == 'west' ):
                self.dungeon.move_hero(action)

            elif action == 'talk':
                self.dungeon.hero.talk()

            elif action == 'help':
                print "Available actions:"
                print "    look                  - look around"
                print "    north|south|east|west - move in this direction"
                print "    talk                  - talk to a monster"
                print "    help                  - print this message"
                print "    quit                  - Exit the game"

            elif action == 'quit':
                exit()



class Dungeon(object):

    def __init__(self, name, entry, hero):
        self.name  = name
        self.entry = entry
        self.hero  = hero


    def enter(self):
        os.system("clear")
        print ("You are %s, a %s %s. Fingering your %s somewhat nervously, you"
              " walk through the %s, and enter %s." 
              % (self.hero.name, self.hero.race, self.hero.occupation,
                 self.hero.weapon, self.entry, self.name ))

        self.hero.current_location = self.rooms[0]


    def store_rooms(self, rooms):
        self.rooms = rooms


    def place_thing(self, thing, room_number):
        self.rooms[room_number].store_thing(thing)


    def move_thing(self, thing, src_room, dest_room):
        thing = src_room.things.pop(thing.name)
        dest_room.store_thing(thing)
        thing.current_location = dest_room


    def move_hero(self, direction):
        if self.hero.current_location.has_an_exit(direction):
            next_room = self.hero.current_location.exits[direction]
            print "You trudge %s." % direction
            self.move_thing(self.hero, self.hero.current_location, next_room)

        else:
            print "You walk into the %s wall. Ouch!" % direction



class Room(object):

    def __init__(self):
        self.exits = dict(
                           north = None,
                           south = None,
                           east  = None,
                           west  = None,
                          )
        self.description = "A non-descript room."

        self.things = {}


    def has_an_exit(self, direction):
        if self.exits.get(direction):
            return True

        return False


    def link_exit_to_room(self, exit, room):
        self.exits[exit] = room

        # Create the corresponding back-link
        backlink_mapping = dict(
                                 north = 'south',
                                 south = 'north',
                                 east  = 'west',
                                 west  = 'east',
                                )
        room.exits[backlink_mapping[exit]] = self


    def store_thing(self, thing):
        self.things[thing.name] = thing


    def get_description(self):
        description = self.description

        description += "\n"
        for thing in self.things.values():
            description += "There is a %s called %s here.\n" % (thing.race, thing.name)

        description += "\n"
        for direction, room in self.exits.items():
            if room:
                description += "There is an exit to the %s.\n" % direction

        return description


    def get_conversationalist(self):
        for thing in self.things.values():
            if thing.can_talk:
                return thing

        return False



class Hero(object):

    def __init__(self, name, race, occupation, weapon):
        self.name             = name
        self.race             = race
        self.occupation       = occupation
        self.weapon           = weapon
        self.current_location = None
        self.can_talk         = False


    def look(self):
        print self.current_location.get_description()


    def talk(self):
        conversationalist = self.current_location.get_conversationalist()

        if conversationalist:
            print conversationalist.talk()

        else:
            print "There doesn't seem to be anyone to talk to here."



class Monster(object):

    def __init__(self, name, race, sex, adjective, talk_phrase):
        self.name             = name
        self.race             = race
        self.sex              = sex
        self.adjective        = adjective
        self.talk_phrase      = talk_phrase
        self.current_location = None
        self.can_talk         = True


    def get_possessive_pronoun(self):
        pronoun_mapping = dict(
                                male   = 'his',
                                female = 'her',
                               )

        return pronoun_mapping[self.sex]


    def description(self):
        description = ("There is a %s %s here. Apparently %s name is '%s'."
                       % (self.adjective, self.race,
                          self.get_possessive_pronoun(), self.name) )

        return description


    def talk(self):
        talk_string = (self.name + ' the ' + self.race + ' says ' 
                       + '"' + self.talk_phrase + '"')

        return talk_string
