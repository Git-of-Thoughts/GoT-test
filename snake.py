class Snake:
    def __init__(self):
        self.body = [(10, 10), (10, 11), (10, 12)]
        self.direction = "UP"

    def move(self):
        head = self.body[0]
        if self.direction == "UP":
            self.body = [(head[0]-1, head[1])] + self.body[:-1]
        elif self.direction == "DOWN":
            self.body = [(head[0]+1, head[1])] + self.body[:-1]
        elif self.direction == "LEFT":
            self.body = [(head[0], head[1]-1)] + self.body[:-1]
        elif self.direction == "RIGHT":
            self.body = [(head[0], head[1]+1)] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def collided_with_self(self):
        return len(self.body) != len(set(self.body))

    def collided_with_wall(self, board_size):
        head = self.body[0]
        return head[0] < 0 or head[1] < 0 or head[0] >= board_size or head[1] >= board_size
