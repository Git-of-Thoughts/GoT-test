from position import Position

class Snake:
    DIRECTIONS = {"w": Position(0, -1), "a": Position(-1, 0),
                  "s": Position(0, 1), "d": Position(1, 0)}

    def __init__(self):
        self.head = Position(0, 0)
        self.body = [self.head]
        self.direction = self.DIRECTIONS["d"]

    def set_direction(self, direction):
        if direction in self.DIRECTIONS:
            self.direction = self.DIRECTIONS[direction]

    def move(self):
        self.head = self.head + self.direction
        self.body.insert(0, self.head)
        return self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])
