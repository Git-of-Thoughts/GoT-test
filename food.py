import random

class Food:
    def __init__(self):
        self.position = (random.randint(0, 19), random.randint(0, 19))

    def generate(self):
        self.position = (random.randint(0, 19), random.randint(0, 19))
