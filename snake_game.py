import random
import curses

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self, length, direction):
        self.length = length
        self.direction = direction
        self.body = [Point(0, i) for i in range(length)]

    def move(self):
        head = self.body[0]
        if self.direction == 'up':
            new_head = Point(head.x - 1, head.y)
        elif self.direction == 'down':
            new_head = Point(head.x + 1, head.y)
        elif self.direction == 'left':
            new_head = Point(head.x, head.y - 1)
        else:  # self.direction == 'right'
            new_head = Point(head.x, head.y + 1)
        self.body.insert(0, new_head)
        self.body.pop()

    def change_direction(self, direction):
        self.direction = direction

    def grow(self):
        self.length += 1
        self.body.append(self.body[-1])

    def collides_with_self(self):
        head = self.body[0]
        return any(point.x == head.x and point.y == head.y for point in self.body[1:])

    def collides_with_wall(self, width, height):
        head = self.body[0]
        return head.x < 0 or head.y < 0 or head.x >= height or head.y >= width

class Game:
    def __init__(self, width, height, snake_length):
        self.width = width
        self.height = height
        self.snake = Snake(snake_length, 'right')
        self.apple = self.spawn_apple()
        self.score = 0

    def play(self):
        curses.initscr()
        win = curses.newwin(self.height, self.width, 0, 0)
        win.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        win.border(0)
        win.nodelay(1)

        while True:
            event = win.getch()
            self.handle_input(event)
            self.update()
            if self.check_collision():
                break
            self.draw(win)

        curses.endwin()

    def draw(self, win):
        win.clear()
        win.border(0)
        win.addch(self.apple.x, self.apple.y, '*')
        for point in self.snake.body:
            win.addch(point.x, point.y, '#')
        win.addstr(0, 2, 'Score : ' + str(self.score) + ' ')
        win.timeout(150 - (len(self.snake.body)//5 + len(self.snake.body)//10)%120)

    def handle_input(self, event):
        if event == ord('w'):
            self.snake.change_direction('up')
        elif event == ord('s'):
            self.snake.change_direction('down')
        elif event == ord('a'):
            self.snake.change_direction('left')
        elif event == ord('d'):
            self.snake.change_direction('right')

    def update(self):
        self.snake.move()
        head = self.snake.body[0]
        if head.x == self.apple.x and head.y == self.apple.y:
            self.score += 1
            self.snake.grow()
            self.apple = self.spawn_apple()

    def check_collision(self):
        return self.snake.collides_with_self() or self.snake.collides_with_wall(self.width, self.height)

    def spawn_apple(self):
        while True:
            x = random.randint(1, self.height - 2)
            y = random.randint(1, self.width - 2)
            if not any(point.x == x and point.y == y for point in self.snake.body):
                return Point(x, y)

def main():
    game = Game(20, 60, 5)
    game.play()

if __name__ == "__main__":
    main()
