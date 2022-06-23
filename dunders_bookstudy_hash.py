class BookStudy:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = int(year)

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))

    def __eq__(self, other):
        return hash(self) == hash(other)
