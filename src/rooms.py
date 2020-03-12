from room import Room
from item import Item

# Declare all the rooms
OUTSIDE = Room("Outside Cave Entrance", "North of you, the cave mount beckons", [
               Item("Flashlight", "How convenient")])

FOYER = Room(
    "Foyer", """Dim light filters in from the south. Dusty passages run north and east.""")

OVERLOOK = Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.", [
                Item('Key', 'Looks ancient. It has a skull engraving on it')])

NARROW = Room("Narrow Passage",
              """The narrow passage bends here from west to north. The smell of gold permeates the air.""")

TREASURE = Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""")


# Link rooms together

OUTSIDE.n_to = FOYER
FOYER.s_to = OUTSIDE
FOYER.n_to = OVERLOOK
FOYER.e_to = NARROW
OVERLOOK.s_to = FOYER
NARROW.w_to = FOYER
NARROW.n_to = TREASURE
TREASURE.s_to = NARROW