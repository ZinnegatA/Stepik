class ItemAttrs:
    def __getitem__(self, item):
        if not isinstance(item, int) or item >= len(self.__dict__):
            raise IndexError('Неверный индекс поля')
        return list(self.__dict__.values())[item]

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key >= len(self.__dict__):
            raise IndexError('Неверный индекс поля')
        setattr(self, list(self.__dict__.keys())[key], value)


class Point(ItemAttrs):
    def __init__(self, x, y):
        if isinstance(x, (int, float)) and isinstance(y, (int, float)):
            self.x = x
            self.y = y
