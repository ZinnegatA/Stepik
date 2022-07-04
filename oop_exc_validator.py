class Validator:
    def __init__(self, min_value, max_value):
        self._min_value = min_value
        self._max_value = max_value
        self._value_type = object

    def __call__(self, value, *args, **kwargs):
        if type(value) is not self._value_type or value < self._min_value or value > self._max_value:
            raise ValueError('значение не прошло валидацию')


class FloatValidator(Validator):
    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)
        self._value_type = float


class IntegerValidator(Validator):
    def __init__(self, min_value, max_value):
        super().__init__(min_value, max_value)
        self._value_type = int


def is_valid(lst, validators):
    def validate(st):
        for validator in validators:
            try:
                validator(st)
                return True
            except ValueError:
                pass

        return False

    return list(filter(validate, lst))
