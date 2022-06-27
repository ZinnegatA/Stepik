class VideoItem:
    def __init__(self, title, descr, path):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating:
    def __init__(self):
        self.__rating = 0

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        if not isinstance(rating, int) or rating not in range(0, 6):
            raise ValueError('Неверное присваиваемое значение')
        self.__rating = rating
