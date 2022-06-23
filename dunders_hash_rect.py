class Rect:
    def __init__(self, x, y, width, height):
        if Rect.check_value(x, y, width, height):
            self.coords = x, y
            self.width = width
            self.height = height

    @staticmethod
    def check_value(*args):
        flag = True
        for arg in args:
            if not isinstance(arg, (int, float)):
                flag = False
        return flag

    def __eq__(self, other):
        return self.width == other.width and self.height == other.height

    def __hash__(self):
        return hash(self.width + self.height)
