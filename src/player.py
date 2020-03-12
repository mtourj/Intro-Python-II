# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, current_room):
    self.current_room = current_room
    self.inventory = []
  
  def travel(self, direction):
    '''Move player in a direction toward a room.
       Returns True on success, False on failure
    '''
    target_room = getattr(self.current_room, f'{direction}_to')
    if target_room:
      self.current_room = target_room
      return True
    else:
      return False

  def addItemToInventory(self, item):
    self.inventory.append(item)

  def removeItemFromInventory(self, item):
    item.on_drop()
    self.inventory.remove(item)

