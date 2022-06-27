class IteratorAttrs:
    def __iter__(self):
        self.indx = -1
        return self

    def __next__(self):
        self.indx += 1
        if self.indx < len(self.__dict__) - 1:
            return list(self.__dict__.items())[self.indx]
        else:
            raise StopIteration


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        if isinstance(model, str) and isinstance(size, tuple) and isinstance(memory, int):
            self.model = model
            self.size = size
            self.memory = memory
