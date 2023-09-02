import random
from point import Point

class Food:
    def __init__(self, board_size):
        self.position = Point(random.randint(0, board_size - 1),
                              random.randint(0, board_size - 1))
