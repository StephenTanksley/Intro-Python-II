# Implement a class to hold room information. This should have name and
# description attributes.
from item import items


class Room:
    def __init__(self, name, description, inventory):
        self.name = name
        self.description = description
        self.inventory = inventory

    def __str__(self):
        return f"{self.name} : {self.description}"

    def __repr__(self):
        return f"self.name = {self.name} self.description = {self.description}"


rooms = {
    'outside':  Room("Outside Cave Entrance\n",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer\n", """Dim light filters in from the south. Dusty
passages run north and east.""", [items['torch']]),

    'overlook': Room("Grand Overlook\n", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["rope"]),

    'narrow':   Room("Narrow Passage\n", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber\n", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}

# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']
