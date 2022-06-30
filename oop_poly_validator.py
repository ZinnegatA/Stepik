class Validator:
    def _is_valid(self, data):
        raise NotImplementedError('В классе не переопределен метод _is_valid')


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, value):
        return isinstance(value, float) and self.min_value <= value <= self.max_value

    def __call__(self, *args, **kwargs):
        return self._is_valid(*args)
