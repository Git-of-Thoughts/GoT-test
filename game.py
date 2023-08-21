import os
import time
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0

    def start(self):
        while True:
            self.update()
            time.sleep(1)

    def end(self):
        print('Game Over! Your score is: ', self.score)

    def draw_board(self):
        os.system('clear')
        for i in range(20):
            for j in range(20):
                if (i, j) in self.snake.body:
                    print('S', end='')
                elif (i, j) == self.food.position:
                    print('F', end='')
                else:
                    print('.', end='')
            print()

    def update(self):
        self.snake.move()
        if self.snake.check_collision():
            self.end()
            exit(0)
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.score += 1
            self.food.generate()
        self.draw_board()
