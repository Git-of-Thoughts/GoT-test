import random

class Snake:
    def __init__(self):
        self.body = [(10, 10), (10, 9), (10, 8)]
        self.direction = 'RIGHT'

    def move(self):
        head = self.body[0]
        if self.direction == 'UP':
            self.body.insert(0, (head[0] - 1, head[1]))
        elif self.direction == 'DOWN':
            self.body.insert(0, (head[0] + 1, head[1]))
        elif self.direction == 'LEFT':
            self.body.insert(0, (head[0], head[1] - 1))
        else:
            self.body.insert(0, (head[0], head[1] + 1))
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def collided_with_self(self):
        return self.body[0] in self.body[1:]
