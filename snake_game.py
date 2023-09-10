import random
import curses

class Snake:
    def __init__(self, window, start_pos):
        self.body = [start_pos]
        self.window = window

    def move(self, direction):
        head = self.body[0]
        new_head = (head[0] + direction[0], head[1] + direction[1])
        self.body.insert(0, new_head)

    def eat(self, food):
        if self.body[0] == food.pos:
            return True
        else:
            self.body.pop()
            return False

    def hit_itself(self):
        return self.body[0] in self.body[1:]

class Food:
    def __init__(self, window, pos=None):
        self.window = window
        if pos is None:
            self.pos = self.random_pos()
        else:
            self.pos = pos

    def random_pos(self):
        return (random.randint(1, self.window.getmaxyx()[0]-2), random.randint(1, self.window.getmaxyx()[1]-2))

class Game:
    def __init__(self, window):
        self.window = window
        self.snake = Snake(window, (10, 10))
        self.food = Food(window)

    def game_loop(self):
        key = curses.KEY_RIGHT
        while True:
            self.window.clear()
            self.window.border(0)
            self.snake.move(self.key_to_direction(key))
            self.window.addch(self.food.pos[0], self.food.pos[1], '#')
            for idx, pos in enumerate(self.snake.body):
                self.window.addch(pos[0], pos[1], '*' if idx == 0 else 'o')
            if self.snake.hit_itself():
                break
            if self.snake.eat(self.food):
                self.food = Food(self.window)
            key = self.window.getch()
            if key == -1:
                continue
            new_direction = self.key_to_direction(key)
            if new_direction[0]*self.key_to_direction(key)[0] + new_direction[1]*self.key_to_direction(key)[1] != 0:
                key = key

    def key_to_direction(self, key):
        return {
            curses.KEY_UP: (-1, 0),
            curses.KEY_DOWN: (1, 0),
            curses.KEY_LEFT: (0, -1),
            curses.KEY_RIGHT: (0, 1)
        }.get(key, (0, 0))

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)
    game = Game(stdscr)
    game.game_loop()

if __name__ == "__main__":
    curses.wrapper(main)
