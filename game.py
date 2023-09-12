import random
from board import Board
from tetrimino import Tetrimino

class Game:
    def __init__(self):
        self.board = Board()
        self.current_tetrimino = self.new_tetrimino()
        self.next_tetrimino = self.new_tetrimino()
        self.score = 0

    def new_tetrimino(self):
        return Tetrimino(random.choice(Tetrimino.SHAPES))

    def start(self):
        while True:
            self.board.add_tetrimino(self.current_tetrimino)
            while not self.board.is_collision(self.current_tetrimino):
                self.board.move_down(self.current_tetrimino)
            self.score += self.board.clear_lines()
            self.current_tetrimino = self.next_tetrimino
            self.next_tetrimino = self.new_tetrimino()
            if self.board.is_collision(self.current_tetrimino):
                break
        print(f"Game Over! Your score is {self.score}")
