class Snake:
    def __init__(self):
        self.positions = [((5, 5))]
        self.direction = (0, -1)

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length() > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0]+x)%20), (cur[1]+y)%20)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length():
                self.positions.pop()

    def reset(self):
        self.positions = [((5, 5))]
        self.direction = (0, -1)

    def length(self):
        return len(self.positions)
