import random
from snake import Snake
from food import Food
from point import Point

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = Snake(Point(width // 2, height // 2))
        self.food = Food(width, height)

    def game_loop(self):
        while True:
            self.snake.move()
            if self.snake.head == self.food.position:
                self.snake.grow()
                self.food = Food(self.width, self.height)
            elif (self.snake.head.x < 0 or self.snake.head.y < 0 or
                  self.snake.head.x >= self.width or self.snake.head.y >= self.height or
                  self.snake.head in self.snake.body[1:]):
                break

if __name__ == "__main__":
    game = Game(20, 20)
    game.game_loop()
