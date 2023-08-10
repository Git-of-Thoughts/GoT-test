import random
import curses

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self, body, direction):
        self.body = body
        self.direction = direction

    def get_head_position(self):
        return self.body[0]

    def turn_left(self):
        self.direction = Point(-1, 0)

    def turn_right(self):
        self.direction = Point(1, 0)

    def turn_up(self):
        self.direction = Point(0, -1)

    def turn_down(self):
        self.direction = Point(0, 1)

    def move(self):
        new_head = Point(self.get_head_position().x + self.direction.x, self.get_head_position().y + self.direction.y)
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def collides_with_self(self):
        return self.get_head_position() in self.body[1:]

class Game:
    def __init__(self, screen, height, width):
        self.screen = screen
        self.height = height
        self.width = width
        self.reset()

    def reset(self):
        self.snake = Snake([Point(self.width // 2, self.height // 2)], Point(0, 0))
        self.score = 0
        self.is_over = False
        self.place_apple()

    def place_apple(self):
        self.apple = Point(random.randint(0, self.width - 1), random.randint(0, self.height - 1))

    def update(self):
        if self.snake.get_head_position() == self.apple:
            self.score += 1
            self.snake.grow()
            self.place_apple()

        if self.snake.get_head_position().x < 0 or self.snake.get_head_position().x >= self.width or self.snake.get_head_position().y < 0 or self.snake.get_head_position().y >= self.height or self.snake.collides_with_self():
            self.is_over = True

        self.snake.move()

    def draw(self):
        self.screen.clear()
        for point in self.snake.body:
            self.screen.addch(point.y, point.x, '#')
        self.screen.addch(self.apple.y, self.apple.x, '*')
        self.screen.addstr(0, 0, 'Score: ' + str(self.score))

def main():
    curses.initscr()
    height, width = 20, 40
    win = curses.newwin(height, width, 0, 0)
    win.keypad(1)
    win.border(0)
    win.nodelay(1)
    game = Game(win, height, width)
    while True:
        event = win.getch()
        if event == ord('q'):
            break
        elif event == curses.KEY_LEFT:
            game.snake.turn_left()
        elif event == curses.KEY_RIGHT:
            game.snake.turn_right()
        elif event == curses.KEY_UP:
            game.snake.turn_up()
        elif event == curses.KEY_DOWN:
            game.snake.turn_down()
        game.update()
        if game.is_over:
            game.reset()
        game.draw()
        win.refresh()
        curses.napms(100)
    curses.endwin()

if __name__ == "__main__":
    main()
