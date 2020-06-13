# Write a class to hold player information, e.g. what room they are in
# currently.

from item import Item


class Player:
    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f'{self.name}: {self.current_room}'

    def __repr__(self):
        return f'self.name = {self.name}, self.current_room = {self.current_room}'

    def grab(self, item):
        print(f'\nYou decide to pick up the {item}.\n')
        self.inventory.append(item)
        self.current_room.inventory.remove(item)
        print(f'Your inventory: {self.inventory}')

    def drop(self, item):
        print(f'\nYou decide to drop the {item}.\n')
        if(len(self.inventory) == 0):
            print("Your satchel is empty already...")
        else:
            self.inventory.remove(item)
            print(f'Your inventory: {self.inventory}')

    def look(self):
        print(
            f'\nScanning the room, you discover a {self.current_room.inventory[0].name}.\n')

    def describe_location(self):
        print(
            f'\n{self.current_room.name} \n{self.current_room.description}\n')
