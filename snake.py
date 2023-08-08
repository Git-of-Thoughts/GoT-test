class Snake:
    def __init__(self):
        self.positions = [(5, 5)]
        self.direction = 'UP'

    def move(self):
        head = self.get_head_position()
        if self.direction == 'UP':
            self.positions.insert(0, (head[0], head[1] - 1))
        elif self.direction == 'DOWN':
            self.positions.insert(0, (head[0], head[1] + 1))
        elif self.direction == 'LEFT':
            self.positions.insert(0, (head[0] - 1, head[1]))
        elif self.direction == 'RIGHT':
            self.positions.insert(0, (head[0] + 1, head[1]))
        self.positions.pop()

    def grow(self):
        tail = self.positions[-1]
        if self.direction == 'UP':
            self.positions.append((tail[0], tail[1] - 1))
        elif self.direction == 'DOWN':
            self.positions.append((tail[0], tail[1] + 1))
        elif self.direction == 'LEFT':
            self.positions.append((tail[0] - 1, tail[1]))
        elif self.direction == 'RIGHT':
            self.positions.append((tail[0] + 1, tail[1]))

    def get_head_position(self):
        return self.positions[0]

    def collide_with_self(self):
        return self.get_head_position() in self.positions[1:]
