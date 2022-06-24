from random import randint


class Ellipse:
    def __init__(self, *args):
        if len(args) == 4:
            self.x1 = args[0]
            self.y1 = args[1]
            self.x2 = args[2]
            self.y2 = args[3]

    def __bool__(self):
        return all((hasattr(self, 'x1'), hasattr(self, 'y1'), hasattr(self, 'x2'), hasattr(self, 'y2')))

    def get_coords(self):
        if not bool(self):
            raise AttributeError('Нет координат для извлечения')
        return self.x1, self.y1, self.x2, self.y2


lst_geom = [Ellipse(), Ellipse(), Ellipse(*[randint(1, 16) for _ in range(4)]),
            Ellipse(*[randint(1, 16) for _ in range(4)])]
for el in lst_geom:
    if bool(el):
        el.get_coords()
