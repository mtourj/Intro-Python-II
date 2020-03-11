# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, current_room):
    self.current_room = current_room
    self.inventory = []
  
  def moveToRoom(self, room):
    self.current_room = room

  def addItemToInventory(self, item):
    self.inventory.append(item)

  def removeItemFromInventory(self, item):
    self.inventory.remove(item)

