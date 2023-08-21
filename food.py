import random

class Food:
    def __init__(self, board_size):
        self.position = (random.randint(0, board_size-1), random.randint(0, board_size-1))

    def randomize_position(self, board_size):
        self.position = (random.randint(0, board_size-1), random.randint(0, board_size-1))
