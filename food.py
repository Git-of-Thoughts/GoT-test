import random

class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        return [random.randint(0, 19), random.randint(0, 19)]
