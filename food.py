import random
from point import Point

class Food:
    def __init__(self, width, height):
        self.position = Point(random.randint(0, width - 1), random.randint(0, height - 1))
