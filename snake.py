class Snake:
    def __init__(self):
        self.length = 1
        self.direction = 'right'
        self.body = [(0, 0)]

    def move(self):
        head = self.body[0]
        if self.direction == 'right':
            new_head = (head[0] + 1, head[1])
        elif self.direction == 'left':
            new_head = (head[0] - 1, head[1])
        elif self.direction == 'up':
            new_head = (head[0], head[1] - 1)
        else:  # self.direction == 'down'
            new_head = (head[0], head[1] + 1)
        self.body.insert(0, new_head)
        if len(self.body) > self.length:
            self.body.pop()

    def grow(self):
        self.length += 1

    def collides_with_self(self):
        return self.body[0] in self.body[1:]

    def collides_with_item(self, item):
        return self.body[0] == item

    def change_direction(self, direction):
        self.direction = direction
