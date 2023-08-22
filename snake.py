from point import Point

class Snake:
    def __init__(self, start_point):
        self.head = start_point
        self.body = [Point(start_point.x, start_point.y - i) for i in range(1, 3)]

    def move(self):
        direction = input("Enter direction (w/a/s/d): ")
        if direction == "w":
            self.head.y -= 1
        elif direction == "a":
            self.head.x -= 1
        elif direction == "s":
            self.head.y += 1
        elif direction == "d":
            self.head.x += 1
        self.body.insert(0, Point(self.head.x, self.head.y))
        self.body.pop()

    def grow(self):
        self.body.append(Point(self.head.x, self.head.y))

    def check_collision(self, grid_size):
        return (self.head in self.body or
                self.head.x < 0 or self.head.y < 0 or
                self.head.x >= grid_size or self.head.y >= grid_size)
