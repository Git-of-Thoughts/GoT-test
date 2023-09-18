import pygame
import time
import random

# Define the dimensions of the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Define the dimensions of the snake and food
SIZE = 20

# Define the colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((WINDOW_WIDTH // 2), (WINDOW_HEIGHT // 2))]
        self.direction = random.choice([up, down, left, right])
        self.color = GREEN

    # Check if the snake has hit itself
    def get_head_position(self):
        return self.positions[0]

    # Update the position of the snake
    def update(self):
        cur = self.get_head_position()
        x,y = self.direction
        new = (((cur[0]+(x*SIZE))%WINDOW_WIDTH), (cur[1]+(y*SIZE))%WINDOW_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()

    # Reset the snake when the game is over
    def reset(self):
        self.length = 1
        self.positions = [((WINDOW_WIDTH // 2), (WINDOW_HEIGHT // 2))]
        self.direction = random.choice([up, down, left, right])

    # Draw the snake
    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], SIZE, SIZE))

class Food:
    def __init__(self):
        self.position = (0,0)
        self.color = RED
        self.randomize_position()

    # Place the food in a random position within the game window
    def randomize_position(self):
        self.position = (random.randint(0, WINDOW_WIDTH-SIZE), random.randint(0, WINDOW_HEIGHT-SIZE))

    # Draw the food
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], SIZE, SIZE))

class Game:
    def __init__(self):
        pygame.init()
        self.snake = Snake()
        self.food = Food()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # Check if the snake has hit the food
    def collision_check(self):
        if self.snake.get_head_position() == self.food.position:
            self.snake.length += 1
            self.food.randomize_position()

    # The main game loop
    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.direction = up
                    elif event.key == pygame.K_DOWN:
                        self.snake.direction = down
                    elif event.key == pygame.K_LEFT:
                        self.snake.direction = left
                    elif event.key == pygame.K_RIGHT:
                        self.snake.direction = right

            self.snake.update()
            self.window.fill(WHITE)
            self.snake.draw(self.window)
            self.food.draw(self.window)
            self.collision_check()
            pygame.display.update()
            clock.tick(5)

if __name__ == "__main__":
    game = Game()
    game.run()
