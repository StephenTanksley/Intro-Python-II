class Item:
    def __init__(self, name, description, quantity):
        self.name = name
        self.description = description
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.quantity} : {self.description}"

    def __repr__(self):
        return f"self.name = {self.name}\n, self.quantity = {self.quantity}\n, self.description = {self.description}"
