import random

class Fruit:
    def __init__(self):
        self.position = [random.randint(0, 19), random.randint(0, 19)]

    def place(self):
        self.position = [random.randint(0, 19), random.randint(0, 19)]
