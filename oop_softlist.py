class SoftList(list):
    def __getitem__(self, item):
        if not isinstance(item, int) or item >= len(self):
            return False
        return super().__getitem__(item)
