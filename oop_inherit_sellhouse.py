class SellItem:
    def __init__(self, name, price):
        if isinstance(name, str) and isinstance(price, (int, float)):
            self.name = name
            self.price = price


class House(SellItem):
    def __init__(self, name, price, material, square):
        super().__init__(name, price)
        self.material = material
        self.square = square


class Flat(SellItem):
    def __init__(self, name, price, size, rooms):
        super().__init__(name, price)
        self.size = size
        self.rooms = rooms


class Land(SellItem):
    def __init__(self, name, price, square):
        super().__init__(name, price)
        self.square = square


class Agency:
    def __init__(self, name):
        if isinstance(name, str):
            self.name = name
        self.objects = []

    def add_object(self, obj):
        if not isinstance(obj, (House, Flat, Land)):
            raise TypeError('Тип данных должен представлять из себя экземпляр класса House, Flat или Land')
        self.objects.append(obj)

    def remove_object(self, obj):
        self.objects.remove(obj)

    def get_objects(self):
        return self.objects
