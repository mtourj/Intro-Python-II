# Implement a class to hold room information. This should have name and
# description attributes.
from colors import Colors


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.__items__ = items

        # Linked rooms
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

    def addItem(self, item):
        '''Add an item to the room'''
        self.__items__.append(item)

    def removeItem(self, item_name):
        '''Remove an item from the room'''
        target_item = None

        # Find item in items
        for item in self.__items__:
            if item.name.lower() == item_name.lower():
                target_item = item
                break

        if(target_item):
            self.__items__.remove(target_item)

        return target_item

    def getItems(self):
        '''Returns items in this room'''
        return self.__items__

    def hasItem(self, item_name):
        '''Checks if this room contains a specific item by name
           Returns True if it exists, False if it does not'''
        return item_name.lower() in [item.name.lower() for item in self.__items__]
