import random

class Fruit:
    def __init__(self, board_size):
        self.position = self.random_position(board_size)

    def random_position(self, board_size):
        return (random.randint(0, board_size - 1), random.randint(0, board_size - 1))
