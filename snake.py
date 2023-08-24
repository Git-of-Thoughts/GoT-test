from point import Point

class Snake:
    def __init__(self, initial_position):
        self.body = [initial_position]
        self.direction = Point(0, 1)

    @property
    def head(self):
        return self.body[0]

    def move(self):
        self.body.insert(0, self.body[0] + self.direction)
        self.body.pop()

    def grow(self):
        self.body.insert(0, self.body[0] + self.direction)

    def change_direction(self, new_direction):
        if (new_direction.x * self.direction.x + new_direction.y * self.direction.y) == 0:
            self.direction = new_direction
