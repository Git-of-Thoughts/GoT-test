import curses
from snake import Snake
from food import Food

class Game:
    def __init__(self, window):
        self.window = window
        self.snake = Snake()
        self.food = Food()

    def start(self):
        while True:
            self.window.clear()
            self.window.border(0)
            self.snake.move()
            if self.snake.body[0] == self.food.position:
                self.snake.grow()
                self.food.place()
            if (self.snake.collided_with_self() or
                self.snake.body[0][0] == 0 or
                self.snake.body[0][0] == 19 or
                self.snake.body[0][1] == 0 or
                self.snake.body[0][1] == 59):
                break
            self.window.addch(self.food.position[0], self.food.position[1], '#')
            for position in self.snake.body:
                self.window.addch(position[0], position[1], '*')
            self.window.refresh()
            curses.napms(100)
