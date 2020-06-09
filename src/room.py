# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name} : {self.description}"

    def __repr__(self):
        return f"self.name = {self.name}\n self.description = {self.description}"


# bedroom = Room("Bedroom", "A room where I go to sleep")

# coordinate = []

# x = 0
# while x < 5:
#     y = 0
#     while y < 4:
#         coordinate.append((x, y))
#         y += 1
#     coordinate.append((x, y))
#     x += 1

# # print(coordinates)
# print(coordinate)
# print(coordinate[1])
# print(coordinate[2])
