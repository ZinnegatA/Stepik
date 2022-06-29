class ShopInterface:
    def get_id(self):
        raise NotImplementedError('В классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    id_obj = 0

    def __init__(self, name, weight, price):
        ShopItem.id_obj += 1
        self._name = name
        self._weight = weight
        self._price = price
        self.__id = ShopItem.id_obj

    def get_id(self):
        return self.__id
