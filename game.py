import random
from snake import Snake
from food import Food
from screen import Screen

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.screen = Screen()
        self.is_game_over = False

    def run(self):
        while not self.is_game_over:
            self.screen.draw(self.snake, self.food)
            self.handle_input()
            self.update()

    def handle_input(self):
        # Handle user input to move the snake

    def update(self):
        # Update the game state
