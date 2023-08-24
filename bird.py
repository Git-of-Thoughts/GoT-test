import pygame

class Bird:
    def __init__(self):
        self.x = 100
        self.y = 300
        self.velocity = 0

    def flap(self):
        self.velocity = -10

    def update(self):
        self.velocity += 1
        self.y += self.velocity

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 20)

    def collides_with(self, pipe):
        return pipe.x < self.x < pipe.x + pipe.width and pipe.y < self.y < pipe.y + pipe.height
