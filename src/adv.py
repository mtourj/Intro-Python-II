from room import Room
from player import Player
import os

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

print('Welcome to the Cave of Lost Treasures\n\
       To play, use W, N, E, S to navigate West, North, East or South\n\
       Press q at any time to quit')

input('Press ENTER to continue...')

error = ''

while True:
    os.system('clear')
    if(len(error) > 0):
        print('\033[1;31;40m' + error + '\n')
        error = ''
    print('\033[1;37;40m' + str(player.current_room))
    user_input = input('(W, N, E, S) >>')

    if(user_input.lower() == 'n'):
        if(player.current_room.n_to == None):
            error = 'There is nothing in that direction.'
        else:
            player.moveToRoom(player.current_room.n_to)
    elif(user_input.lower() == 's'):
        if(player.current_room.s_to == None):
            error = 'There is nothing in that direction.'
        else:
            player.moveToRoom(player.current_room.s_to)
    elif(user_input.lower() == 'w'):
        if(player.current_room.w_to == None):
            error = 'There is nothing in that direction.'
        else:
            player.moveToRoom(player.current_room.w_to)
    elif(user_input.lower() == 'e'):
        if(player.current_room.e_to == None):
            error = 'There is nothing in that direction.'
        else:
            player.moveToRoom(player.current_room.e_to)
    elif(user_input.lower() == 'q'):
        exit()
    else:
        error = 'Invalid input.\nValid inputs: W (West), N (North), E (East), S (South)'
