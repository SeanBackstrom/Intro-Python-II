from player import Player
from room import Room
import types
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 
                     [Item('map', 'Map to another treasure buried somewhere else')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you,
    falling into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from
     west to north. The smell of gold permeates the air."""),

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

# Main


player = Player(room['outside'])


leave = True

while leave:

    currentroom = player.location
    print(currentroom.name, ",", currentroom.description)

    inp = input()
    """
        player controls. possibilities are:
        n - north
        s - south
        e - east
        w - west 
        q- quit
    """
    if inp == "i":
        print("Inventory")
        print("----------")
        for index, item in enumerate(player.items):
            print(f"{index+1}, {item.name}")

    elif inp == "n":
        edge_check = player.location.n_to

        if isinstance(edge_check, types.MethodType) == True:
            pass
        else:
            player.location = player.location.n_to



    elif inp == "s":
        edge_check = player.location.s_to

        if isinstance(edge_check, types.MethodType) == True:
            pass
        else:
            player.location = player.location.s_to


    elif inp == "e":
        edge_check = player.location.e_to

        if isinstance(edge_check, types.MethodType) == True:
            pass
        else:
            player.location = player.location.e_to


    elif inp == "w":
        edge_check = player.location.w_to

        if isinstance(edge_check, types.MethodType) == True:
            pass
        else:
            player.location = player.location.w_to

    elif inp == "q":
        print("The torment is too much. You end your life.")
        leave = False

    elif inp == 'search':
        for item in player.location.items:
            item.on_take(player)
    
    elif inp == "drop":
        for item in player.items:
            item.on_drop(player)
        
    