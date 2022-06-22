class Lib:
    def __init__(self):
        self.book_list = []

    def __len__(self):
        return len(self.book_list)

    def __add__(self, other):
        if not isinstance(other, Book):
            raise TypeError('Операнд справа должен быть экземпляром класса Book')
        self.book_list.append(other)
        return self

    def __sub__(self, other):
        if not isinstance(other, (int, Book)):
            raise TypeError('Операнд справа должен быть int или экземпляром класса Book')
        if isinstance(other, Book):
            self.book_list.remove(other)
        else:
            if other < len(self.book_list):
                del self.book_list[other]
        return self


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
