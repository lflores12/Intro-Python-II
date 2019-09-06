from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# Making a list of all the items in the game
all_items = {
    'sword': Item('sword', 'a sharp sword'),
    'shield': Item('shield', 'a shield to protect you from the unknown'),
    'map': Item('map', 'a map to help guide you through the rooms and to the treasure!'),
    'flashlight': Item('flashlight', 'a small flashlight to help you in the dark rooms. Careful though, it doesnt have much battery left'),
    'treasure': Item('treasure', 'Treasure chest that is empty!'),
}

# Assigning the items to specific rooms
room['outside'].items.append(all_items['sword'])
room['outside'].items.append(all_items['flashlight'])
room['foyer'].items.append(all_items['shield'])


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player('Leo', room['outside'])
new_player.print_current_room()

# strip()
# lower()
# split()

d = input("[N]orth  \n[E]ast   \n[S]outh    \n[W]est    \n[Q]uit\n[I]nventory \nYou can also take an item from a room 'take'' *item name'\n Or drop an item 'drop' '*item name'")

d = d.lower().strip().split()

allowed_commands = ['n', 's', 'w', 'e', 'i', 'take', 'drop']

# Write a loop that:
while 'q' not in d:
    if len(d) == 1:
        if d[0] in allowed_commands:
            if d[0] == 'i':
                new_player.print_inventory()
            else:
                direction = d[0]
                new_player.move_player(direction)
        else:
            print('\nPlease enter a valid direction')
    elif len(d) == 2:
        item = d[1]
        print(item)
        if 'take' in d:
            new_player.take_item(item)
        elif 'drop' in d:
            new_player.drop_item(item)
            # dropped_item.on_drop()
        else:
            print('\nYou do dot have that item in your inventory')
    else:
        print('You cannot perform that action')
    new_player.print_current_room()
    print('What do you want to do next?')
    d = input("[N]orth  \n[E]ast   \n[S]outh    \n[W]est    \n[Q]uit\n[I]nventory\n").lower(
    ).strip().split()


# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
