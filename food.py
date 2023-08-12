import random
from point import Point

class Food:
    def __init__(self, game_width, game_height):
        self.position = Point(random.randint(0, game_width - 1), random.randint(0, game_height - 1))
