import pygame

class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = (10, 0)

    def update(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(None)

    def collides_with(self, other):
        return self.body[0] == other.position

    def draw(self, surface):
        for part in self.body:
            pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(part[0], part[1], 10, 10))
