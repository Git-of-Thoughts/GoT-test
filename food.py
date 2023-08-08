import pygame
import random

class Food:
    def __init__(self):
        self.position = (random.randint(0, 79) * 10, random.randint(0, 59) * 10)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(self.position[0], self.position[1], 10, 10))
