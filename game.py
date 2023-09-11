import os
import time
import curses
from snake import Snake
from apple import Apple

class Game:
    def __init__(self, window):
        self.window = window
        self.snake = Snake()
        self.apple = Apple()

    def draw(self):
        self.window.clear()
        for segment in self.snake.get_body():
            self.window.addch(segment[0], segment[1], '#')
        self.window.addch(self.apple.get_position()[0], self.apple.get_position()[1], '@')
        self.window.refresh()

    def game_over(self):
        head = self.snake.get_head_position()
        return (head in self.snake.get_body()[1:]) or (head[0] < 0 or head[0] > 19 or head[1] < 0 or head[1] > 19)

    def run(self):
        while True:
            self.draw()
            self.window.timeout(100)
            event = self.window.getch()

            if event == curses.KEY_UP:
                self.snake.change_direction('UP')
            elif event == curses.KEY_DOWN:
                self.snake.change_direction('DOWN')
            elif event == curses.KEY_LEFT:
                self.snake.change_direction('LEFT')
            elif event == curses.KEY_RIGHT:
                self.snake.change_direction('RIGHT')

            if self.snake.get_head_position() == self.apple.get_position():
                self.snake.grow()
                self.apple.regenerate()

            self.snake.move()

            if self.game_over():
                break

            time.sleep(0.1)

def main():
    curses.initscr()
    window = curses.newwin(20, 20, 0, 0)
    window.keypad(True)
    game = Game(window)
    game.run()
    curses.endwin()

if __name__ == "__main__":
    main()
