import curses
import random

class Snake:
    def __init__(self, window):
        self.body = [[10, 10], [10, 9], [10, 8]]
        self.window = window

    def move(self, direction):
        head = list(self.body[0])
        if direction == 'up':
            head[0] -= 1
        elif direction == 'down':
            head[0] += 1
        elif direction == 'left':
            head[1] -= 1
        elif direction == 'right':
            head[1] += 1
        self.body.insert(0, head)

    def grow(self):
        self.body.append(self.body[-1])

    def collided_with_self(self):
        return self.body[0] in self.body[1:]

class Apple:
    def __init__(self, window):
        self.window = window
        self.place()

    def place(self):
        height, width = self.window.getmaxyx()
        self.position = [random.randint(1, height - 2), random.randint(1, width - 2)]

class Game:
    def __init__(self, window):
        self.window = window
        self.snake = Snake(window)
        self.apple = Apple(window)

    def start(self):
        self.window.timeout(100)
        while True:
            self.window.clear()
            self.window.border(0)
            self.snake.move(self.get_direction())
            if self.snake.collided_with_self():
                break
            if self.snake.body[0] == self.apple.position:
                self.snake.grow()
                self.apple.place()
            self.draw()

    def get_direction(self):
        key = self.window.getch()
        if key in [curses.KEY_UP, ord('w')]:
            return 'up'
        elif key in [curses.KEY_DOWN, ord('s')]:
            return 'down'
        elif key in [curses.KEY_LEFT, ord('a')]:
            return 'left'
        elif key in [curses.KEY_RIGHT, ord('d')]:
            return 'right'

    def draw(self):
        for part in self.snake.body:
            self.window.addch(part[0], part[1], '#')
        self.window.addch(self.apple.position[0], self.apple.position[1], '@')

def main():
    curses.initscr()
    window = curses.newwin(20, 60, 0, 0)
    window.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    window.border(0)
    game = Game(window)
    game.start()
    curses.endwin()

if __name__ == "__main__":
    main()
