class Thing:
    def __init__(self, name, weight):
        if isinstance(name, str) and isinstance(weight, float):
            self.name = name
            self.weight = weight


class ArtObject(Thing):
    def __init__(self, name, weight, author, date):
        super().__init__(name, weight)
        if isinstance(author, str) and isinstance(date, str):
            self.author = author
            self.date = date


class Computer(Thing):
    def __init__(self, name, weight, memory, CPU):
        super().__init__(name, weight)
        if isinstance(memory, int) and isinstance(CPU, str):
            self.memory = memory
            self.CPU = CPU


class Auto(Thing):
    def __init__(self, name, weight, dims):
        super().__init__(name, weight)
        if isinstance(dims, tuple):
            self.dims = dims


class Mercedes(Auto):
    def __init__(self, name, weight, dims, model, old):
        super().__init__(name, weight, dims)
        if isinstance(model, str) and isinstance(old, int):
            self.model = model
            self.old = old


class Toyota(Auto):
    def __init__(self, name, weight, dims, model, wheel):
        super().__init__(name, weight, dims)
        if isinstance(model, str) and isinstance(wheel, bool):
            self.model = model
            self.wheel = wheel
