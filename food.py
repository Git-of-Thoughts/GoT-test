import random

class Food:
    def __init__(self, grid_size):
        self.position = self.random_position(grid_size)

    def random_position(self, grid_size):
        return (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
