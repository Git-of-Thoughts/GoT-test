import curses
from random import randint

class Snake:
    def __init__(self):
        self.body = [(10, 10), (10, 9), (10, 8)]
        self.direction = curses.KEY_RIGHT

    def change_direction(self, key):
        if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
            self.direction = key

    def move(self):
        head = self.body[0]
        if self.direction == curses.KEY_RIGHT:
            new_head = (head[0], head[1] + 1)
        elif self.direction == curses.KEY_LEFT:
            new_head = (head[0], head[1] - 1)
        elif self.direction == curses.KEY_UP:
            new_head = (head[0] - 1, head[1])
        elif self.direction == curses.KEY_DOWN:
            new_head = (head[0] + 1, head[1])

        if new_head in self.body or new_head[0] in [0, 20] or new_head[1] in [0, 60]:
            return "COLLISION"
        else:
            self.body.insert(0, new_head)
            self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def draw(self, screen):
        for part in self.body:
            screen.addch(part[0], part[1], '#')

