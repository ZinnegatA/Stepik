class Course:
    def __init__(self, name):
        self.name = name
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)

    def remove_module(self, indx):
        del self.modules[indx]


class Module:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson):
        self.lessons.append(lesson)

    def remove_lesson(self, indx):
        del self.lessons[indx]


class LessonItem:
    dct_type = {'title': (str,), 'practices': (int,), 'duration': (int,)}

    def __setattr__(self, key, value):
        if type(value) not in self.dct_type[key]:
            raise TypeError('Неверный тип присваиваемых данных.')
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item in ('title', 'practices', 'duration'):
            raise AttributeError("Атрибут удалять запрещено.")

    def __init__(self, title, practices, duration):
        self.title = title
        self.practices = practices
        self.duration = duration
