class Person:
    __slots__ = '_fio', '_old', '_job'

    def __init__(self, fio, old, job):
        if isinstance(fio, str) and isinstance(old, int) and isinstance(job, str) and old > 0:
            self._fio = fio
            self._old = old
            self._job = job


person1 = Person('Путин', 62, 'президент РФ')
person2 = Person('Шойгу', 60, 'министр обороны РФ')
person3 = Person('Балакирев', 34, 'программист и преподаватель')
person4 = Person('Пушкин', 32, 'поэт и писатель')
persons = [person1, person2, person3, person4]
