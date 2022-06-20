class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1:
            self.coords = (0 for _ in range(args[0]))
        else:
            self.coords = args

    def set_coords(self, *args):
        self.coords = args

    def get_coords(self):
        return self.coords

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        from math import sqrt
        return sqrt(sum([x ** 2 for x in self.coords]))
