from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    @staticmethod
    def get_info():
        return 'Базовый класс Model'


class ModelForm(Model):
    model_id = 0

    def __init__(self, login, password):
        ModelForm.model_id += 1
        self._login = login
        self._password = password
        self._id = ModelForm.model_id

    def get_pk(self):
        return self._id
