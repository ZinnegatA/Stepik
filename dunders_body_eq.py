class Body:
    def __init__(self, name, ro, volume):
        if isinstance(name, str) and isinstance(ro, (int, float)) and isinstance(volume, (int, float)):
            self.name = name
            self.ro = ro
            self.volume = volume

    def __gt__(self, other):
        if not isinstance(other, (int, float, Body)):
            raise TypeError(
                'Правый операнд должен быть либо целым или вещественным числом, либо экземпляром класса Body')
        sc = other.ro * other.volume if type(other) is Body else other
        return self.ro * self.volume > sc

    def __lt__(self, other):
        if not isinstance(other, (int, float, Body)):
            raise TypeError(
                'Правый операнд должен быть либо целым или вещественным числом, либо экземпляром класса Body')
        sc = other.ro * other.volume if type(other) is Body else other
        return self.ro * self.volume < sc

    def __eq__(self, other):
        if not isinstance(other, (int, float, Body)):
            raise TypeError(
                'Правый операнд должен быть либо целым или вещественным числом, либо экземпляром класса Body')
        sc = other.ro * other.volume if type(other) is Body else other
        return self.ro * self.volume == sc
