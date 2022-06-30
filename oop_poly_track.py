class Track:
    def __init__(self, *args):
        if len(args) == 2:
            self.__points = [PointTrack(*args)]
        else:
            self.__points = list(args)

    @property
    def points(self):
        return tuple(self.__points)

    def add_back(self, pt):
        self.__points.append(pt)

    def add_front(self, pt):
        self.__points.insert(0, pt)

    def pop_back(self):
        del self.__points[-1]

    def pop_front(self):
        del self.__points[0]


class PointTrack:
    def __init__(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError('Координаты должны быть числами')
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.__class__}: {self.x}, {self.y}"
