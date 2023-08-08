import pygame
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.snake = Snake()
        self.food = Food()

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            self.snake.update()
            if self.snake.collides_with(self.food):
                self.snake.grow()
                self.food = Food()
            self.screen.fill((0, 0, 0))
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            pygame.display.flip()
            clock.tick(60)
