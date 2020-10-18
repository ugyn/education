# https://stepik.org/lesson/24461/step/9?unit=6767

class Buffer:
    def __init__(self):
        self.array = []

    def add(self, *a):
        self.array += a
        while len(self.array) >= 5:
            s = 0
            for n in self.array[0:5]:
                s += n
            print(s)
            del self.array[0:5]

    def get_current_part(self):
        return self.array
