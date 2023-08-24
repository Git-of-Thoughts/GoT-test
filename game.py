import pygame
import sys
from snake import Snake
from food import Food

class Game:
    def __init__(self, screen_width=800, screen_height=600):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction('up')
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction('down')
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction('left')
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction('right')

    def update(self):
        self.snake.move()
        if self.snake.head_position() == self.food.position:
            self.snake.grow()
            self.food.randomize_position()

    def render(self):
        self.screen.fill((0, 0, 0))
        for position in self.snake.body:
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(position[0], position[1], 10, 10))
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.food.position[0], self.food.position[1], 10, 10))
        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(30)
