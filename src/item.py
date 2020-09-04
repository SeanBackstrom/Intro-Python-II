from player import Player

class Item:
    """controls operation of picking up an item or dropping"""
    def __init__(self, name, description):
        self.name = name
        self.description = description

    '''
    def isinroom(self):
        is_iteminroom = False
        if self.location == Player.location:
            is_iteminroom = True
            return is_iteminroom
        else:
            is_iteminroom = False
            return is_iteminroom
            '''
    def on_take(self, player):
        player.items.append(self)
        player.location.items.remove(self)
        print(f"You picked up {self.name}")
    
    def on_drop(self, player):
        player.items.remove(self)
        player.location.items.append(self)
        print(f"You dropped {self.name}")
