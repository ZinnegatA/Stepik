class Validator:
    data_type = None

    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data):
        if isinstance(data, self.data_type) and self.min_value <= data <= self.max_value:
            return True
        raise ValueError('Введенные данные не прошли валидацию')

    def __call__(self, data):
        return self._is_valid(data)


class IntegerValidator(Validator):
    data_type = int


class FloatValidator(Validator):
    data_type = float
