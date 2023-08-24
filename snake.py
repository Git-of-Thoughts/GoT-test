class Snake:
    def __init__(self):
        self.direction = 'right'
        self.body = [(100, 100), (90, 100), (80, 100)]

    def change_direction(self, direction):
        self.direction = direction

    def move(self):
        head = self.body[0]
        if self.direction == 'up':
            new_head_position = (head[0], head[1]-10)
        elif self.direction == 'down':
            new_head_position = (head[0], head[1]+10)
        elif self.direction == 'left':
            new_head_position = (head[0]-10, head[1])
        elif self.direction == 'right':
            new_head_position = (head[0]+10, head[1])
        self.body.insert(0, new_head_position)
        self.body.pop()

    def grow(self):
        self.body.append(None)

    def head_position(self):
        return self.body[0]

    def hit_itself(self):
        return self.head_position() in self.body[1:]
