class Digit:
    def __init__(self, value):
        self.check(value)
        self.value = value

    def check(self, value):
        if type(value) not in [int, float]:
            raise TypeError('значение не соответствует типу объекта')


class Integer(Digit):
    def __init__(self, value):
        super().__init__(value)

    def check(self, value):
        if type(value) != int:
            raise TypeError('значение не соответствует типу объекта')


class Float(Digit):
    def __init__(self, value):
        super().__init__(value)

    def check(self, value):
        if type(value) != float:
            raise TypeError('значение не соответствует типу объекта')


class Positive(Digit):
    def __init__(self, value):
        super().__init__(value)

    def check(self, value):
        if value < 0:
            raise TypeError('значение не соответствует типу объекта')


class Negative(Digit):
    def __init__(self, value):
        super().__init__(value)

    def check(self, value):
        if value > 0:
            raise TypeError('значение не соответствует типу объекта')


class PrimeNumber(Integer, Positive):
    def __init__(self, value):
        super().__init__(value)


class FloatPositive(Float, Positive):
    def __init__(self, value):
        super().__init__(value)


digits = [PrimeNumber(5), PrimeNumber(5), PrimeNumber(5),
          FloatPositive(0.5),
          FloatPositive(0.5),
          FloatPositive(0.5),
          FloatPositive(0.5),
          FloatPositive(0.5)]

lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
lst_float = list(filter(lambda x: isinstance(x, Float), digits))
