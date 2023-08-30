class Snake:
    def __init__(self):
        self.body = [(10, 10), (10, 11), (10, 12)]
        self.direction = "N"

    def move(self):
        head = self.body[0]
        if self.direction == "N":
            self.body = [(head[0]-1, head[1])] + self.body[:-1]
        elif self.direction == "S":
            self.body = [(head[0]+1, head[1])] + self.body[:-1]
        elif self.direction == "E":
            self.body = [(head[0], head[1]+1)] + self.body[:-1]
        elif self.direction == "W":
            self.body = [(head[0], head[1]-1)] + self.body[:-1]

    def grow(self):
        self.body.append(self.body[-1])

    def collided_with_self(self):
        return len(self.body) != len(set(self.body))
