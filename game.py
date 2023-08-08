from board import Board
from snake import Snake
from apple import Apple

class Game:
    def __init__(self, board_size):
        self.board = Board(board_size)
        self.snake = Snake()
        self.apple = Apple(self.board)

    def play(self):
        while True:
            self.board.draw(self.snake, self.apple)
            direction = input("Enter direction (up, down, left, right): ")
            self.snake.move(direction)
            if self.board.check_collision(self.snake):
                print("Game over!")
                break
            if self.snake.head == self.apple.position:
                self.snake.grow()
                self.apple.place_new()

if __name__ == "__main__":
    game = Game(10)
    game.play()
