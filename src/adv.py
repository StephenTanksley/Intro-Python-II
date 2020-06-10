from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance\n",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer\n", """Dim light filters in from the south. Dusty
passages run north and east.""", ["torch"]),

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

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


def create_player():
    initiate_player = input("What is your name? - ").capitalize()
    return Player(initiate_player, room['outside'], [])


def main():
    player = create_player()
    print(player.grab)
    print(f"Welcome to the game, {player.name}.")
    print(f"You are in {player.current_room}.")

    playing = True
    while playing:
        choice = input(
            "Choose a direction - 'n', 's', 'e', 'w', or 'quit' to quit: ").lower()

        command_string = choice.split(' ')
        print(command_string)

        # check to see if the input direction is N, S, E, W - If so,
        try:
            if(choice == 'n'):
                player.current_room = player.current_room.n_to
                print(player.current_room)

            elif(choice == 's'):
                player.current_room = player.current_room.s_to
                print(player.current_room)

            elif(choice == 'e'):
                player.current_room = player.current_room.e_to
                print(player.current_room)

            elif(choice == 'w'):
                player.current_room = player.current_room.w_to
                print(player.current_room)

            elif(choice == 'look'):
                print(player.current_room.inventory)

            elif(command_string[0] == 'grab'):
                player.grab(command_string[1])
                player.current_room.inventory.remove(command_string[1])
                print('Your inventory: ', player.inventory)
                print('Room\'s inventory: ', player.current_room.inventory)

            elif(choice == 'quit'):
                playing = False

        except Exception:
            print("That is not a valid command.")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


if __name__ == '__main__':
    main()
