# https://stepik.org/lesson/24461/step/8?unit=6767

class MoneyBox:

    def __init__(self, capacity):
        self.capacity = capacity
        self.s = 0

    def can_add(self, v):
        if self.s + v <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        self.s += v


