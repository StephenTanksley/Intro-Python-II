# Write a class to hold player information, e.g. what room they are in
# currently.

from item import Item


class Player:
    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory  # [items...]

        # self.grab():
        # grab something from the room's inventory, place into player inventory
        # self.drop()
        # opposite of grab.

    def __str__(self):
        return f"{self.name}: {self.current_room}"

    def __repr__(self):
        return f"self.name = {self.name}\n, self.current_room = {self.current_room}"

    def grab(self, item):
        self.inventory.append(item)
