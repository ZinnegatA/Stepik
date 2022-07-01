class Money:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Сумма должна быть числом')
        self._money = value

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, value):
        self._money = value


class MoneyOperators:
    def __add__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money + other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money + other.money)

    def __sub__(self, other):
        if type(other) in (int, float):
            return self.__class__(self.money - other)

        if type(self) != type(other):
            raise TypeError('Разные типы объектов')

        return self.__class__(self.money - other.money)
