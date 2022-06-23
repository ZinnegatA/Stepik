class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}

    def write(self, record):
        self.dict_db.setdefault(record, []).append(record)

    def read(self, pk):
        for elem in self.dict_db:
            if elem.pk == pk:
                return elem


class Record:
    unique_id = 0

    def __init__(self, fio, descr, old):
        Record.unique_id += 1
        self.pk = Record.unique_id
        self.fio = fio
        self.descr = descr
        self.old = old

    def __hash__(self):
        return hash((self.fio.lower(), self.old))

    def __eq__(self, other):
        return hash(self) == hash(other)
