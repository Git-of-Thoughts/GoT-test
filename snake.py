from point import Point

class Snake:
    def __init__(self, start):
        self.body = [start]
        self.direction = Point(0, 1)

    def head(self):
        return self.body[0]

    def move(self):
        self.body.insert(0, self.body[0] + self.direction)
        self.body.pop()

    def grow(self):
        self.body.insert(0, self.body[0] + self.direction)

    def self_collision(self):
        return self.head() in self.body[1:]

    def in_bounds(self, size):
        return 0 <= self.head().x < size and 0 <= self.head().y < size

    def on_body(self, point):
        return point in self.body
