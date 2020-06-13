from room import rooms
from player import Player
from item import items

# Declare all the rooms


# room = {
#     'outside':  Room("Outside Cave Entrance\n",
#                      "North of you, the cave mount beckons", []),

#     'foyer':    Room("Foyer\n", """Dim light filters in from the south. Dusty
# passages run north and east.""", [items['torch']]),

#     'overlook': Room("Grand Overlook\n", """A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm.""", ["rope"]),

#     'narrow':   Room("Narrow Passage\n", """The narrow passage bends here from west
# to north. The smell of gold permeates the air.""", []),

#     'treasure': Room("Treasure Chamber\n", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south.""", []),
# }

# # Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']


def create_player():
    initiate_player = input("\nWhat is your name? - ").capitalize()
    return Player(initiate_player, rooms['outside'], [])


def main():
    player = create_player()
    print(f'\nWelcome to the game, {player.name}.\n')
    print(
        f'\nYou are in {player.current_room.name} \n{player.current_room.description}\n')

    playing = True
    while playing:
        choice = input(
            "\tChoose a direction - 'n', 's', 'e', 'w', or 'quit' to quit: ").lower()
        command_string = choice.split(' ')

        try:
            if(choice in ['n', 's', 'e', 'w']):
                if hasattr(player.current_room, f'{choice}_to'):
                    player.current_room = getattr(
                        player.current_room, f'{choice}_to')
                    player.describe_location()
                elif not hasattr(player.current_room, f'{choice}_to'):
                    print(
                        "\nYou search in vain for a way forward. Try another direction.\n")

            elif(command_string[0] == 'look'):
                player.describe_location()
                player.look()

            elif(command_string[0] == 'grab'):
                player.grab(command_string[1])
                player.current_room.inventory.remove(command_string[1])

            elif(command_string[0] == 'drop'):
                player.drop(command_string[1])
                player.current_room.inventory.append(command_string[1])

            elif(choice == 'quit'):
                playing = False

        except Exception as inst:
            print('error type: ', type(inst))
            print('more information: ', inst.args)
            print("Your eyes deceive you, squire. Try again.")


if __name__ == '__main__':
    main()
