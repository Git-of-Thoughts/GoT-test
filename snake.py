from point import Point

class Snake:
    def __init__(self):
        self.direction = Point(1, 0)
        self.head = Point(0, 0)
        self.body = []

    def move(self):
        self.body.insert(0, self.head)
        self.head += self.direction
        self.body.pop()

    def grow(self):
        self.body.insert(0, self.head)
        self.head += self.direction
