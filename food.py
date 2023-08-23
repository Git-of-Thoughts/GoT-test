import curses
from random import randint

class Food:
    def __init__(self):
        self.position = (randint(1, 19), randint(1, 59))

    def draw(self, screen):
        screen.addch(self.position[0], self.position[1], '*')

