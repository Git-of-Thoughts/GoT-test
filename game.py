import pygame
from pygame.locals import *
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        pygame.init()
        self.snake = Snake()
        self.food = Food()

    def check_for_collision(self):
        if self.snake.get_head_position() == self.food.position:
            self.snake.length += 1
            self.food.randomize_position()

    def run(self):
        clock = pygame.time.Clock()
        surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake Game')

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.snake.turn(UP)
                    elif event.key == K_DOWN:
                        self.snake.turn(DOWN)
                    elif event.key == K_LEFT:
                        self.snake.turn(LEFT)
                    elif event.key == K_RIGHT:
                        self.snake.turn(RIGHT)

            self.snake.move()
            self.check_for_collision()
            surface.fill((0,0,0))
            self.snake.draw(surface)
            self.food.draw(surface)
            pygame.display.update()
            clock.tick(5 + self.snake.length//10)
