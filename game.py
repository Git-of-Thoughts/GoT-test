import pygame
from fruit import Fruit

class Game:
    def __init__(self):
        self.board = [[None for _ in range(4)] for _ in range(4)]
        self.add_fruit()

    def add_fruit(self):
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.board[i][j] is None]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.board[i][j] = Fruit()

    def update(self):
        # Handle game logic here

    def draw(self):
        # Draw game board here
