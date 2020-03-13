from room import Room
from player import Player
from item import Item
from views import SceneManager
import rooms

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(rooms.OUTSIDE)

print('Welcome to the Cave of Lost Treasures\n\
       To play, use W, N, E, S to navigate West, North, East or South\n\
       Press q at any time to quit')

input('Press ENTER to continue...')

# Error to display
error = ''

# When this is true, we are on the
# 'inventory screen', so to speak
viewInventory = False

# Valid movement inputs
move_directions = ('n', 's', 'e', 'w')

while True:
    # Show error if any
    if(len(error) > 0):
        SceneManager.alert(error)
        error = ''
    
    # Conditional render - Inventory or Room
    if(viewInventory):
        SceneManager.renderInventory(player.inventory)
    else:
        SceneManager.renderRoom(player.current_room)


    # Get user input...
    user_input = input('(W, N, E, S) >>')

    # Command formatted to lower case, split by space
    command = user_input.lower().split(' ')

    # If it is in move_directions, it is a move command
    if(command[0] in move_directions):
        moved = player.travel(command[0])
        if not moved:
            error = 'There is nothing in that direction.'
    # Pick up an item
    elif(command[0] == 'take' or command[0] == 'get'):
        if(len(command) < 2):
            error = f'Invalid input.\nUsage: {command[0]} [item] - Pick up an item in the room'
        else:
            # Does this item exist in the room?
            if(player.current_room.hasItem(command[1])):
                item = player.current_room.removeItem(command[1])
                player.addItemToInventory(item)
            else:
                error = f'There is not a(n) {command[1]} here'
    # Drop an item
    elif(command[0] == 'drop'):
        if(len(command) < 2):
            error = f'Invalid input.\nUsage: drop [item] - Drop an item from inventory'
        else:
            # Does the player have this item?
            if(player.hasItem(command[1])):
                item = player.removeItemFromInventory(command[1])
                player.current_room.addItem(item)
            else:
                error = f'You do not have a(n) {command[1]}'
    # Toggle inventory view
    elif(command[0] == 'i' or command[0] == 'inventory'):
        viewInventory = not viewInventory
    # Exit application
    elif(command[0] == 'q'):
        exit(0)
    # Invalid input, display an error
    else:
        error = 'Invalid input.\nValid inputs: W (West), N (North), E (East), S (South)'
