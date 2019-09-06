# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def print_current_room(self):
        print(self.current_room)

    def take_item(self, item):
        for i in self.current_room.items:
            if i.name == item:
                self.items.append(i)
                i.on_take()
                self.current_room.items.remove(i)

            else:
                return print('*That item is not in this room')

    def move_player(self, direction):
        if getattr(self.current_room, f'{direction}_to') is not None:
            self.current_room = getattr(self.current_room, f'{direction}_to')
        else:
            print("Cant go that way")

    def drop_item(self, item):
        for i in self.items:
            if i.name == item:
                self.items.remove(i)
                i.on_drop()
                self.current_room.items.append(i)
            else:
                return print('You do not have that item in your inventory')

    def print_inventory(self):
        if len(self.items) >= 1:
            print(f'Items in Inventory: {self.items}')
        else:
            print('You have no items in your Inventory!')

    def find_item(self, item):
        for i in self.items:
            if i.name == item:
                return i
            else:
                print("Print you dont not have that item in your inventory")
