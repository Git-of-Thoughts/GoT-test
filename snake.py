from direction import Direction
from point import Point

class Snake:
    def __init__(self, initial_position):
        self.body = [initial_position]
        self.direction = Direction.RIGHT

    def move(self):
        head = self.get_head()
        if self.direction == Direction.UP:
            self.body.insert(0, Point(head.x, head.y - 1))
        elif self.direction == Direction.DOWN:
            self.body.insert(0, Point(head.x, head.y + 1))
        elif self.direction == Direction.LEFT:
            self.body.insert(0, Point(head.x - 1, head.y))
        elif self.direction == Direction.RIGHT:
            self.body.insert(0, Point(head.x + 1, head.y))
        self.body.pop()

    def grow(self):
        tail = self.body[-1]
        self.body.append(Point(tail.x, tail.y))

    def get_head(self):
        return self.body[0]

    def collided_with_self(self):
        return self.get_head() in self.body[1:]
