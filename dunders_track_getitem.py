class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.coords = []

    def add_point(self, x, y, speed):
        self.coords.append([(x, y), speed])

    def __getitem__(self, item):
        if item >= len(self.coords):
            raise IndexError('Некорректный индекс')
        return self.coords[item]

    def __setitem__(self, key, value):
        if key >= len(self.coords):
            raise IndexError('Некорректный индекс')
        self.coords[key][1] = value
