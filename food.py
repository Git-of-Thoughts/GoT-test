import random

class Food:
    def __init__(self):
        self.position = (random.randint(1, 18), random.randint(1, 58))

    def place(self):
        self.position = (random.randint(1, 18), random.randint(1, 58))
