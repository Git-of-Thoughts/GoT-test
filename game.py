import random
from snake import Snake
from grid import Grid

class Game:
    def __init__(self, grid_size):
        self.grid = Grid(grid_size)
        self.snake = Snake(self.grid)
        self.food = None
        self.generate_food()

    def start(self):
        while True:
            self.update()

    def end(self):
        print("Game Over!")
        exit(0)

    def generate_food(self):
        while True:
            position = (random.randint(0, self.grid.size - 1), random.randint(0, self.grid.size - 1))
            if position not in self.snake.body:
                self.food = position
                break

    def update(self):
        self.snake.move()
        if self.snake.head == self.food:
            self.snake.grow()
            self.generate_food()
        elif self.snake.check_collision():
            self.end()
        self.grid.draw(self.snake, self.food)

def main():
    game = Game(10)
    game.start()

if __name__ == "__main__":
    main()
