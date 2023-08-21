import random
import curses

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self, head, body):
        self.head = head
        self.body = body
        self.direction = Point(0, 1)

    def move(self):
        self.body.insert(0, self.head.copy())
        self.head.x += self.direction.x
        self.head.y += self.direction.y

    def grow(self):
        self.body.append(self.body[-1].copy())

    def collided_with_self(self):
        return self.head in self.body

class Game:
    def __init__(self, screen):
        self.score = 0
        self.screen = screen
        self.snake = Snake(Point(10, 10), [Point(10, 9), Point(10, 8)])
        self.apple = Point(random.randint(1, 18), random.randint(1, 58))

    def draw(self):
        self.screen.clear()
        for part in self.snake.body:
            self.screen.addch(part.x, part.y, '#')
        self.screen.addch(self.snake.head.x, self.snake.head.y, '*')
        self.screen.addch(self.apple.x, self.apple.y, '@')

    def update(self):
        if self.snake.head == self.apple:
            self.score += 1
            self.snake.grow()
            self.apple = Point(random.randint(1, 18), random.randint(1, 58))
        else:
            self.snake.move()

    def handle_input(self, key):
        new_direction = Point(0, 0)
        if key == curses.KEY_DOWN:
            new_direction = Point(1, 0)
        elif key == curses.KEY_UP:
            new_direction = Point(-1, 0)
        elif key == curses.KEY_LEFT:
            new_direction = Point(0, -1)
        elif key == curses.KEY_RIGHT:
            new_direction = Point(0, 1)

        if (new_direction.x * -1, new_direction.y * -1) != (self.snake.direction.x, self.snake.direction.y):
            self.snake.direction = new_direction

    def run(self):
        while True:
            self.screen.nodelay(1)
            self.screen.border(0)
            self.draw()
            self.screen.refresh()
            key = self.screen.getch()

            if key != -1:
                self.handle_input(key)

            self.update()

            if self.snake.collided_with_self():
                break

def main():
    curses.initscr()
    win = curses.newwin(20, 60, 0, 0)
    win.keypad(1)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.nodelay(1)

    game = Game(win)
    game.run()

    curses.endwin()

if __name__ == "__main__":
    main()
