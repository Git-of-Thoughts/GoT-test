import random

class Apple:
    def __init__(self):
        self.position = (random.randint(0, 19), random.randint(0, 19))

    def regenerate(self):
        self.position = (random.randint(0, 19), random.randint(0, 19))

    def get_position(self):
        return self.position
