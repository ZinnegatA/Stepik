class DigitRetrieve:
    def __call__(self, string, *args, **kwargs):
        return int(string) if string.lstrip('-').isdigit() else None


dg = DigitRetrieve()
st = ["123", "abc", "-56.4", "0", "-5"]
digits = list(map(dg, st))
print(digits)
