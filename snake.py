class Snake:
    def __init__(self):
        self.body = [(0, 0)]
        self.directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

    @property
    def head(self):
        return self.body[0]

    def move(self, direction):
        new_head = (self.head[0] + self.directions[direction][0],
                    self.head[1] + self.directions[direction][1])
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.insert(0, self.body[0])
