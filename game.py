import pygame
from bird import Bird
from pipe import Pipe

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.bird = Bird()
        self.pipes = [Pipe()]

    def run(self):
        running = True
        while running:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.bird.flap()
            self.update()
            self.draw()
        pygame.quit()

    def update(self):
        self.bird.update()
        for pipe in self.pipes:
            pipe.update()
            if pipe.collides_with(self.bird):
                self.game_over()

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.bird.draw(self.screen)
        for pipe in self.pipes:
            pipe.draw(self.screen)
        pygame.display.flip()

    def game_over(self):
        print("Game Over!")
        pygame.quit()
