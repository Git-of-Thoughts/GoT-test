class Snake:
    def __init__(self):
        self.positions = [[5, 5]]
        self.direction = 'U'

    def move(self):
        head = self.get_head_position()
        if self.direction == 'U':
            self.positions.insert(0, [head[0]-1, head[1]])
        elif self.direction == 'D':
            self.positions.insert(0, [head[0]+1, head[1]])
        elif self.direction == 'L':
            self.positions.insert(0, [head[0], head[1]-1])
        elif self.direction == 'R':
            self.positions.insert(0, [head[0], head[1]+1])
        self.positions.pop()

    def grow(self):
        head = self.get_head_position()
        if self.direction == 'U':
            self.positions.insert(0, [head[0]-1, head[1]])
        elif self.direction == 'D':
            self.positions.insert(0, [head[0]+1, head[1]])
        elif self.direction == 'L':
            self.positions.insert(0, [head[0], head[1]-1])
        elif self.direction == 'R':
            self.positions.insert(0, [head[0], head[1]+1])

    def get_head_position(self):
        return self.positions[0]

    def collide_with_self(self):
        return self.get_head_position() in self.positions[1:]
