from room import Room
from player import Player
from item import Item
from colors import Colors
import os

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Crate", 'I am box')]),

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

os.system('clear')

error = ''

while True:
    if(len(error) > 0):
        print(Colors.RED + error + '\n')
        error = ''
    print(Colors.WHITE + str(player.current_room))
    user_input = input('(W, N, E, S) >>')

    os.system('clear')
    command = user_input.lower().split(' ')

    if(command[0] == 'n'):
        if(player.current_room.n_to == None):
            error = 'There is nothing in that direction.'
        else:
            player.moveToRoom(player.current_room.n_to)
    elif(command[0] == 's'):
        if(player.current_room.s_to == None):
            error = 'There is nothing in that direction.'
        else:
            player.moveToRoom(player.current_room.s_to)
    elif(command[0] == 'w'):
        if(player.current_room.w_to == None):
            error = 'There is nothing in that direction.'
        else:
            player.moveToRoom(player.current_room.w_to)
    elif(command[0] == 'e'):
        if(player.current_room.e_to == None):
            error = 'There is nothing in that direction.'
        else:
            player.moveToRoom(player.current_room.e_to)
    elif(command[0] == 'take' or command[0] == 'get'):
        if(len(command) < 2):
            error = f'Invalid input.\nUsage: {command[0]} [item] - Pick up an item in the room'
        else:
            targetItem = command[1]
            for item in player.current_room.items:
                if(item.name.lower() == targetItem):
                    player.current_room.removeItem(item)
                    player.addItemToInventory(item)
                    # Set item to empty string to know if we've found it
                    targetItem = ''
            if(len(targetItem) > 0):
                error = f'There is not a(n) {targetItem} here'
    elif(command[0] == 'drop'):
        if(len(command) < 2):
            error = f'Invalid input.\nUsage: drop [item] - Drop an item from inventory'
        else:
            targetItem = command[1]
            for item in player.inventory:
                if(item.name.lower() == targetItem):
                    player.removeItemFromInventory(item)
                    player.current_room.addItem(item)
                    # Set item to empty string to know if we've found it
                    targetItem = ''
            if(len(targetItem) > 0):
                error = f'You do not have a(n) {targetItem}'
    elif(command[0] == 'q'):
        exit()
    else:
        error = 'Invalid input.\nValid inputs: W (West), N (North), E (East), S (South)'
