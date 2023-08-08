import random

class Food:
    def __init__(self, board_size):
        self.position = self.generate_food(board_size)

    def generate_food(self, board_size):
        return (random.randint(0, board_size - 1), random.randint(0, board_size - 1))

    def get_position(self):
        return self.position
