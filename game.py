import os
import time
from snake import Snake
from food import Food

class Game:
    def __init__(self, game_width=20, game_height=20):
        self.game_width = game_width
        self.game_height = game_height
        self.snake = Snake()
        self.food = Food(game_width, game_height)

    def draw(self):
        os.system('clear')
        for i in range(self.game_height):
            for j in range(self.game_width):
                if (i, j) in self.snake.body:
                    print('S', end='')
                elif (i, j) == self.food.position:
                    print('F', end='')
                else:
                    print('.', end='')
            print()

    def update(self):
        self.snake.move()
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food.place(self.game_width, self.game_height)

    def is_game_over(self):
        head = self.snake.body[0]
        return (head[0] < 0 or head[1] < 0 or head[0] >= self.game_width or head[1] >= self.game_height or self.snake.collided_with_self())

    def play(self):
        while not self.is_game_over():
            self.draw()
            self.update()
            time.sleep(0.2)
