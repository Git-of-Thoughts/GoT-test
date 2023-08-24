import random

class Food:
    def __init__(self):
        self.position = (0, 0)

    def place(self, snake_body):
        while True:
            x = random.randint(0, 19)
            y = random.randint(0, 19)
            if (x, y) not in snake_body:
                self.position = (x, y)
                break
