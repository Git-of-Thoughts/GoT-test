import random

class Food:
    def __init__(self):
        self.position = (random.randint(0, 10), random.randint(0, 10))

    def reposition(self):
        self.position = (random.randint(0, 10), random.randint(0, 10))
