import pygame
import random

class Pipe:
    def __init__(self):
        self.x = 800
        self.y = random.randint(100, 500)
        self.width = 100
        self.height = random.randint(100, 300)
        self.velocity = -5

    def update(self):
        self.x += self.velocity

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.width, self.height))

    def collides_with(self, bird):
        return bird.x < self.x < bird.x + bird.width and bird.y < bird.y < bird.y + bird.height
