class Dimensions:
    def __setattr__(self, key, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Габаритные размеры должны быть целыми или вещественными положительными числами")
        object.__setattr__(self, key, value)

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __le__(self, other):
        return hash(self) <= hash(other)

    def __lt__(self, other):
        return hash(self) < hash(other)


lst_dims = sorted(Dimensions(*map(float, line.split())) for line in input().split(';'))
