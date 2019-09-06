# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = []

    def find_item(self, item):
        for i in self.items:
            if i.name == item:
                return i
            else:
                print('That item is not in this room')

    def __str__(self):
        return f'Room Name: {self.name} \nDescription:{self.description} \nItems in Room: {self.items}'

    def __repr__(self):
        return f'Room({repr(self.name)}, {repr(self.description)})'
