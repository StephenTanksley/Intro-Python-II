# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, inventory):
        self.name = name
        self.description = description
        self.inventory = inventory

    def __str__(self):
        return f"{self.name} : {self.description}"

    def __repr__(self):
        return f"self.name = {self.name} self.description = {self.description}"
