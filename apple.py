import random
from point import Point

class Apple:
    def __init__(self, grid_size):
        self.position = Point(random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
