class Snake:
    def __init__(self):
        self.positions = [(5, 5)]
        self.direction = (0, -1)

    def move(self):
        head = self.positions[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.positions.insert(0, new_head)
        self.positions.pop()

    def grow(self):
        head = self.positions[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.positions.insert(0, new_head)

    def collides_with_self(self):
        return self.positions[0] in self.positions[1:]
