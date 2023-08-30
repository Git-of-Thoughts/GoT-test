from snake import Snake
from fruit import Fruit
from board import Board

class Game:
    def __init__(self, board_size):
        self.snake = Snake()
        self.fruit = Fruit(board_size)
        self.board = Board(board_size, self.snake, self.fruit)
        self.score = 0

    def start(self):
        while True:
            self.board.draw()
            self.board.update()
            if self.snake.collided_with_self() or self.snake.collided_with_edge(self.board.size):
                break
            if self.snake.body[0] == self.fruit.position:
                self.score += 1
        print("Game over! Your score was: ", self.score)

    def end(self):
        print("Thanks for playing!")

if __name__ == "__main__":
    game = Game(20)
    game.start()
    game.end()
