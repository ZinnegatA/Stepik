class AnimalDescriptor:
    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Animal:
    name = AnimalDescriptor()
    kind = AnimalDescriptor()
    old = AnimalDescriptor()

    def __init__(self, name, kind, old):
        if isinstance(name, str) and isinstance(kind, str) and isinstance(old, int):
            self.name = name
            self.kind = kind
            self.old = old


animals = [Animal('Васька', 'дворовый кот', 5), Animal('Рекс', 'немецкая овчарка', 8), Animal('Кеша', 'попугай', 3)]
