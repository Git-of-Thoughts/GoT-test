class Snake:
    def __init__(self):
        self.length = 1
        self.direction = 'right'
        self.body = [(10, 10)]

    def move(self):
        head = self.body[0]
        if self.direction == 'up':
            self.body.insert(0, (head[0], head[1] - 1))
        elif self.direction == 'down':
            self.body.insert(0, (head[0], head[1] + 1))
        elif self.direction == 'left':
            self.body.insert(0, (head[0] - 1, head[1]))
        elif self.direction == 'right':
            self.body.insert(0, (head[0] + 1, head[1]))
        if len(self.body) > self.length:
            self.body.pop()

    def grow(self):
        self.length += 1

    def check_collision(self):
        return self.body[0] in self.body[1:] or self.body[0][0] < 0 or self.body[0][0] >= 20 or self.body[0][1] < 0 or self.body[0][1] >= 20
