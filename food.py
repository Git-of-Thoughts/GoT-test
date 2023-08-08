import random

class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        # Return a random position for the food
