from colors import Colors

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
      print(f'{Colors.GREEN}You picked up: {self.name} - {self.description}\n')