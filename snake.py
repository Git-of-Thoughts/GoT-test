class Snake:
    def __init__(self):
        self.body = [(10, 10), (10, 11), (10, 12)]
        self.direction = "UP"

    def move(self):
        head = self.get_head()
        if self.direction == "UP":
            self.body.insert(0, (head[0] - 1, head[1]))
        elif self.direction == "DOWN":
            self.body.insert(0, (head[0] + 1, head[1]))
        elif self.direction == "LEFT":
            self.body.insert(0, (head[0], head[1] - 1))
        elif self.direction == "RIGHT":
            self.body.insert(0, (head[0], head[1] + 1))
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def get_head(self):
        return self.body[0]

    def has_collided_with_self(self):
        return self.get_head() in self.body[1:]
