class Snake:
    def __init__(self):
        self.length = 1
        self.direction = "right"
        self.body = [(10, 10)]

    def move(self):
        head = self.body[0]
        if self.direction == "right":
            new_head = (head[0], head[1] + 1)
        elif self.direction == "left":
            new_head = (head[0], head[1] - 1)
        elif self.direction == "up":
            new_head = (head[0] - 1, head[1])
        elif self.direction == "down":
            new_head = (head[0] + 1, head[1])
        self.body.insert(0, new_head)
        if len(self.body) > self.length:
            self.body.pop()

    def grow(self):
        self.length += 1

    def collided_with_self(self):
        return len(self.body) != len(set(self.body))

    def collided_with_edge(self, board_size):
        head = self.body[0]
        return head[0] < 0 or head[1] < 0 or head[0] >= board_size or head[1] >= board_size
