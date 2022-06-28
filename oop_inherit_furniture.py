class Furniture:
    def __init__(self, name, weight):
        self.__verify_name(name)
        self.__verify_weight(weight)
        self._name = name
        self._weight = weight

    @classmethod
    def __verify_name(cls, name):
        if type(name) != str:
            raise TypeError('название должно быть строкой')

    @classmethod
    def __verify_weight(cls, weight):
        if type(weight) not in (int, float) or weight <= 0:
            raise TypeError('вес должен быть положительным числом')

    def get_attrs(self):
        return self.__dict__.values()


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square
