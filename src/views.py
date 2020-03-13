from colors import Colors
import os

class SceneManager:
    '''This `static` class will manage anything that
       gets printed. Handles all renders'''

    __alert__ = ''
    __current__ = None

    @classmethod
    def __render__(cls, view):
        # Render a scene - Print a string onto
        # console and save as most recent view
        os.system('clear')
        if(cls.__alert__):
            print(cls.__alert__ + '\n')
            cls.__alert__ = ''
        print(f'{Colors.WHITE}{view}')
        cls.__current__ = view

    @classmethod
    def alert(cls, message, color=Colors.RED):
        '''Queues an alert with a custom message & color
           Last queued alert will be displayed on next render
           Colors defaults to Colors.RED'''
        cls.__alert__ = f'{color}{message}'

    @classmethod
    def renderRoom(cls, room):
        '''Render a room onto the console'''

        items = ''

        if(len(room.__items__) > 0):
            items = 'There are some things here:\n'
            for item in room.__items__:
                items = items + f'  {item.name}\n'
            items = items + f'\n{Colors.GRAY}Hint: take [item] to take an item'

        # Render result
        cls.__render__(
            f'========================================\n\
{room.name}                             \n\
                                        \n\
{room.description}                      \n\n\
{items}                                 \n\
{Colors.WHITE}========================================\n')

    @classmethod
    def renderInventory(cls, inventory):
        '''Render inventory onto the console'''
        cls.__current__ = inventory

        inventory_contents = ''

        if(len(inventory) == 0):
            inventory_contents = f'{Colors.GRAY}  <You are empty handed>'
        else:
            for item in inventory:
                inventory_contents = inventory_contents + '  ' + \
                    item.name + ' - ' + item.description + '\n'

        # Render result
        cls.__render__(f'========================================\n\
Inventory:\n{inventory_contents}\n\n\
{Colors.GRAY}Use `inventory` or `i` to exit inventory\n\
{Colors.WHITE}========================================\n')
