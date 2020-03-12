# Implement a class to hold room information. This should have name and
# description attributes.
from colors import Colors


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

    def __str__(self):
        items = ''

        if(len(self.items) > 0):
            items = 'There are some things here:\n'
            for item in self.items:
                items = items + f'  {item.name}\n'
            items = items + f'\n{Colors.GRAY}Hint: take [item] to take an item'

        return \
            f'========================================\n\
{self.name}                             \n\
                                        \n\
{self.description}                      \n\n\
{items}                                 \n\
{Colors.WHITE}========================================\n'

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        item.on_take()
        item = self.items.remove(item)
