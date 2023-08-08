import os
import time
import curses

from snake import Snake
from food import Food

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.snake = Snake()
        self.food = Food()

    def run(self):
        while True:
            self.draw()
            self.handle_input()
            self.update()
            time.sleep(0.1)

    def draw(self):
        self.screen.clear()
        for position in self.snake.positions:
            self.screen.addch(position[0], position[1], '#')
        self.screen.addch(self.food.position[0], self.food.position[1], '*')
        self.screen.refresh()

    def handle_input(self):
        key = self.screen.getch()
        if key == curses.KEY_UP:
            self.snake.direction = (-1, 0)
        elif key == curses.KEY_DOWN:
            self.snake.direction = (1, 0)
        elif key == curses.KEY_LEFT:
            self.snake.direction = (0, -1)
        elif key == curses.KEY_RIGHT:
            self.snake.direction = (0, 1)

    def update(self):
        self.snake.move()
        if self.snake.positions[0] == self.food.position:
            self.snake.grow()
            self.food.randomize_position()
        if self.snake.collides_with_self():
            self.reset()

    def reset(self):
        self.snake = Snake()
        self.food = Food()

def main():
    curses.wrapper(Game)
