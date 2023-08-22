import time
from snake import Snake
from food import Food
from board import Board

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.board = Board(self.snake, self.food)
        self.score = 0

    def start(self):
        while True:
            self.board.display_board()
            time.sleep(1)
            self.snake.move()
            if self.snake.get_head_position() == self.food.position:
                self.snake.grow()
                self.score += 1
                self.food = Food()
            self.board.update_board()
            if self.game_over():
                break
        print(f'Game Over! Your score is: {self.score}')

    def game_over(self):
        head = self.snake.get_head_position()
        return (head[0] < 0 or head[0] >= 20 or head[1] < 0 or head[1] >= 20 or self.snake.collide_with_self())
