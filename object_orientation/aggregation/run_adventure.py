#!/usr/bin/env python

'''
run_adventure.py - Simple command line adventure game.

Author: Eric Saunders
February 2011
'''

from dungeon import *

# Create some core game elements: a hero, a dungeon, and a monster
hero    = Hero(name="Michelle", race="Halfling", 
               occupation="Data Visualisation Engineer", weapon="cellphone")

dungeon = Dungeon(name="the grim fortress of LCOGT",
                  entry="keycard-protected but inexplicably ajar front door",
                  hero = hero)

monster = Monster(name="Andrew", race="Goblin", sex="male", adjective="slimy",
                  talk_phrase="It's just a script. How hard can it be?")


# Construct some rooms
rooms = [Room() for i in range(4)]

# Link the rooms
# 0 -- 2
# |    |
# 1 -- 3
rooms[0].link_exit_to_room('south', rooms[1])
rooms[0].link_exit_to_room('east',  rooms[2])
rooms[1].link_exit_to_room('east',  rooms[3])
rooms[2].link_exit_to_room('south', rooms[3])

# Add the rooms, hero and monster to the dungeon
dungeon.store_rooms(rooms)
dungeon.place_thing(hero, room_number=0)
dungeon.place_thing(monster, room_number=3)

# Add the dungeon to the game
game = Game(dungeon)

# Run the configured game
game.run_game_loop()

