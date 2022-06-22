class Budget:
    def __init__(self):
        self.items = list()

    def add_item(self, it):
        if isinstance(it, Item):
            self.items.append(it)

    def remove_item(self, indx):
        if isinstance(indx, int) and 0 <= indx < len(self.items):
            del self.items[indx]

    def get_items(self):
        return self.items

    def __iter__(self):
        return iter(self.items)


class Item:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def __add__(self, other):
        if isinstance(other, (self.__class__, int)):
            return self.money + other

    def __radd__(self, other):
        return self + other
