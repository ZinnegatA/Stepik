class Record:
    def __init__(self, **kwargs):
        for key, value in dict(kwargs).items():
            setattr(self, key, value)

    def __getitem__(self, item):
        if not isinstance(item, int) or item >= len(self.__dict__):
            raise IndexError('Неверный индекс поля')
        return [value for value in self.__dict__.values()][item]

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key >= len(self.__dict__):
            raise IndexError('Неверный индекс поля')
        setattr(self, list(self.__dict__.keys())[key], value)
