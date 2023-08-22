import random
from snake import Snake
from apple import Apple
from point import Point

class Game:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.snake = Snake(Point(grid_size // 2, grid_size // 2))
        self.apple = Apple(self.grid_size)

    def game_loop(self):
        while True:
            self.snake.move()
            if self.snake.head == self.apple.position:
                self.snake.grow()
                self.apple = Apple(self.grid_size)
            elif self.snake.check_collision(self.grid_size):
                break
            self.draw()

    def draw(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                point = Point(i, j)
                if self.snake.head == point:
                    print("S", end="")
                elif point in self.snake.body:
                    print("s", end="")
                elif self.apple.position == point:
                    print("A", end="")
                else:
                    print(".", end="")
            print()

if __name__ == "__main__":
    game = Game(10)
    game.game_loop()
