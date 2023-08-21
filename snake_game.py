import curses
import random

class Snake:
    def __init__(self, window, start_coord):
        self.body = [start_coord]
        self.window = window

    def move(self, direction):
        head = self.body[0]
        if direction == 'up':
            new_head = (head[0]-1, head[1])
        elif direction == 'down':
            new_head = (head[0]+1, head[1])
        elif direction == 'left':
            new_head = (head[0], head[1]-1)
        elif direction == 'right':
            new_head = (head[0], head[1]+1)
        self.body.insert(0, new_head)

    def grow(self):
        self.body.append(self.body[-1])

    def collided_with_self(self):
        return self.body[0] in self.body[1:]

class Food:
    def __init__(self, window, snake):
        self.window = window
        self.snake = snake
        self.place_food()

    def place_food(self):
        while True:
            x = random.randint(1, self.window.getmaxyx()[0]-2)
            y = random.randint(1, self.window.getmaxyx()[1]-2)
            if (x, y) not in self.snake.body:
                self.food = (x, y)
                break

class Game:
    def __init__(self, window):
        self.window = window
        self.snake = Snake(self.window, (10, 10))
        self.food = Food(self.window, self.snake)

    def start(self):
        self.window.timeout(100)
        while True:
            self.window.clear()
            self.window.border(0)
            self.snake.move(self.get_direction())
            if self.snake.collided_with_self():
                break
            if self.snake.body[0] == self.food.food:
                self.snake.grow()
                self.food.place_food()
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
        else:
            return 'up'

    def draw(self):
        for part in self.snake.body:
            self.window.addch(part[0], part[1], '#')
        self.window.addch(self.food.food[0], self.food.food[1], '*')

def main():
    curses.initscr()
    window = curses.newwin(20, 60, 0, 0)
    window.keypad(True)
    game = Game(window)
    game.start()
    curses.endwin()

if __name__ == "__main__":
    main()
