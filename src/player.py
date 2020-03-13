# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.inventory = []

    def travel(self, direction):
        '''Move player in a direction toward a room.
           Returns True on success, False on failure'''
        target_room = getattr(self.current_room, f'{direction}_to')
        if target_room:
            self.current_room = target_room
            return True
        else:
            return False

    def addItemToInventory(self, item):
        '''Add item to player's inventory
          by instance'''
        item.on_take()
        self.inventory.append(item)

    def removeItemFromInventory(self, item_name):
        '''Remove an item from player's inventory
          by name'''
        target_item = None

        # Find item in inventory
        for item in self.inventory:
            if(item.name.lower() == item_name.lower()):
                target_item = item
                break

        if(target_item):
            item.on_drop()
            self.inventory.remove(item)

        return target_item

    def hasItem(self, item_name):
        '''Checks if this player has a specific item by name
           Returns True if it exists, False if it does not'''
        return item_name.lower() in [item.name.lower() for item in self.inventory]
