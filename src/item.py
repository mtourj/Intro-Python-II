from colors import Colors
from views import SceneManager

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        SceneManager.alert(f'You picked up: {self.name} - {self.description}\n\
Use `inventory` to see inventory', Colors.GREEN)

    def on_drop(self):
        SceneManager.alert(f'You dropped {self.name}', Colors.YELLOW)
