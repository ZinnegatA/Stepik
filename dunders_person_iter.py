class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job

    def __getitem__(self, item):
        if not isinstance(item, int) or item not in range(0, 5):
            raise IndexError('Неверный индекс')
        return [value for value in self.__dict__.values()][item]

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key not in range(0, 5):
            raise IndexError('Неверный индекс')
        setattr(self, list(self.__dict__.keys())[key], value)

    def __iter__(self):
        self.indx = -1
        return self

    def __next__(self):
        if self.indx < 4:
            self.indx += 1
            return list(self.__dict__.values())[self.indx]
        raise StopIteration
