class PolyLine:
    def __init__(self, *args):
        self.coords = list(args)
        self.start_coord = self.coords[0]

    def add_coord(self, x, y):
        self.coords.append((x, y))

    def remove_coord(self, indx):
        del self.coords[indx]

    def get_coords(self):
        return self.coords
