class Box:
    def __init__(self):
        self.things_list = []

    def add_thing(self, obj):
        if type(obj) is Thing:
            self.things_list.append(obj)

    def get_things(self):
        return self.things_list

    def __eq__(self, other):
        if not isinstance(other, Box):
            raise TypeError('Правый операнд должен являться экземпляром класса Box')
        return sorted(self.things_list) == sorted(other.things_list)


class Thing:
    def __init__(self, name, mass):
        if isinstance(name, str) and isinstance(mass, (int, float)):
            self.name = name
            self.mass = mass

    def __eq__(self, other):
        if not isinstance(other, Thing):
            raise TypeError('Правый операнд должен являться экземпляром класса Thing')
        return self.name.lower() == other.name.lower() and self.mass == other.mass

    def __lt__(self, other):
        if type(other) is Thing:
            return (self.name, self.mass) < (other.name, other.mass)
