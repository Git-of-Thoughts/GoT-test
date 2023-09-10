import random

class Fruit:
    def __init__(self):
        self.position = (0, 0)
        self.set_position()

    def set_position(self):
        x = random.randint(0, 19)
        y = random.randint(0, 19)
        self.position = (x, y)

    def get_position(self):
        return self.position
