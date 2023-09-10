import curses
from snake import Snake
from fruit import Fruit

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.snake = Snake()
        self.fruit = Fruit()

    def draw(self, pos, ch):
        x, y = pos
        self.screen.addch(int(y), int(x), ch)

    def handle_keys(self):
        key = self.screen.getch()
        if key == curses.KEY_UP:
            self.snake.turn((0, -1))
        elif key == curses.KEY_DOWN:
            self.snake.turn((0, 1))
        elif key == curses.KEY_LEFT:
            self.snake.turn((-1, 0))
        elif key == curses.KEY_RIGHT:
            self.snake.turn((1, 0))

    def play(self):
        while True:
            self.screen.clear()
            self.handle_keys()
            self.snake.move()
            if self.snake.get_head_position() == self.fruit.get_position():
                self.fruit.set_position()
            else:
                self.draw(self.fruit.get_position(), '#')
            for pos in self.snake.positions:
                self.draw(pos, '*')
            self.screen.refresh()
