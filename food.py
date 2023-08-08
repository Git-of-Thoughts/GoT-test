import random

class Food:
    def __init__(self, board_width, board_height):
        self.position = (random.randint(0, board_width - 1), random.randint(0, board_height - 1))

    def reset_position(self):
        self.position = (random.randint(0, board_width - 1), random.randint(0, board_height - 1))
