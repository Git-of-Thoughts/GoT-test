import os
import time
import keyboard

from snake import Snake
from food import Food
from board import Board

class Game:
    def __init__(self, board_width, board_height):
        self.snake = Snake()
        self.food = Food(board_width, board_height)
        self.board = Board(board_width, board_height, self.snake, self.food)

    def start(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.board.draw()
            if self.game_over():
                break
            self.update()
            time.sleep(0.2)

    def update(self):
        if keyboard.is_pressed('up'):
            self.snake.direction = 'UP'
        elif keyboard.is_pressed('down'):
            self.snake.direction = 'DOWN'
        elif keyboard.is_pressed('left'):
            self.snake.direction = 'LEFT'
        elif keyboard.is_pressed('right'):
            self.snake.direction = 'RIGHT'
        self.snake.move()
        if self.snake.get_head_position() == self.food.position:
            self.snake.grow()
            self.food.reset_position()

    def game_over(self):
        x, y = self.snake.get_head_position()
        return x < 0 or y < 0 or x >= self.board.width or y >= self.board.height or self.snake.collide_with_self()
