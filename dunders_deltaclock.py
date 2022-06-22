class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds


class DeltaClock:
    def __init__(self, clock1: Clock, clock2: Clock):
        self.clock1 = clock1
        self.clock2 = clock2

    def __len__(self):
        result = self.clock1.get_time() - self.clock2.get_time()
        if result < 0:
            return 0
        return result

    def __str__(self):
        time = self.__len__()
        hours = time // 3600
        minutes = (time - hours * 3600) // 60
        seconds = time - hours * 3600 - minutes * 60

        return f"{hours if hours > 9 else '0' + str(hours)}: " \
               f"{minutes if minutes > 9 else '0' + str(minutes)}: " \
               f"{seconds if seconds > 9 else '0' + str(seconds)}"
