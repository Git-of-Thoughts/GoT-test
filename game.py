import time
from snake import Snake
from fruit import Fruit
from board import Board

class Game:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.board = Board(self.snake, self.fruit)
        self.score = 0

    def run(self):
        while True:
            self.board.update()
            self.board.print()
            time.sleep(0.1)
            self.snake.move()
            if self.snake.get_head_position() == self.fruit.position:
                self.snake.grow()
                self.fruit.place()
                self.score += 1
            if self.snake.collide_with_self():
                break
        print(f'Game Over! Your score is: {self.score}')

if __name__ == "__main__":
    game = Game()
    game.run()
