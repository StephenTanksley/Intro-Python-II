class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

    def __repr__(self):
        return f"self.name = {self.name}, self.description = {self.description}"


class LightSource(Item):
    def __init__(self, name, description, illuminated):
        super().__init__(name, description)
        self.illuminated = illuminated

    def __str__(self):
        return f'{self.name} lit? {self.illuminated}'

    def light(self, name):
        if (self.illuminated == False):
            self.illuminated = True
            print(f"You lit the {self.name}")


items = {
    'torch': LightSource(
        'torch', 'A simple torch waiting to be lit.', False),
}
