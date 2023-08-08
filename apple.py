import random

class Apple:
    def __init__(self, board):
        self.board = board
        self.place_new()

    def place_new(self):
        while True:
            position = (random.randint(0, self.board.size - 1),
                        random.randint(0, self.board.size - 1))
            if position not in self.board.snake.body:
                self.position = position
                break
