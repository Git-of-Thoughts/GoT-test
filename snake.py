class Snake:
    def __init__(self, grid):
        self.grid = grid
        self.direction = "right"
        self.body = [(0, 0)]
        self.head = self.body[0]

    def move(self):
        if self.direction == "up":
            self.head = (self.head[0] - 1, self.head[1])
        elif self.direction == "down":
            self.head = (self.head[0] + 1, self.head[1])
        elif self.direction == "left":
            self.head = (self.head[0], self.head[1] - 1)
        elif self.direction == "right":
            self.head = (self.head[0], self.head[1] + 1)
        self.body.insert(0, self.head)

    def grow(self):
        pass

    def check_collision(self):
        return self.head in self.body[1:] or not (0 <= self.head[0] < self.grid.size and 0 <= self.head[1] < self.grid.size)
