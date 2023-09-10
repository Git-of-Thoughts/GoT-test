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
        self.alive = True

class Game:
    def __init__(self, screen, height=20, width=60):
        self.screen = screen
        self.height = height
        self.width = width
        self.snake = Snake([Point(width//2, height//2)], 'RIGHT')
        self.food = self.new_food()
        self.score = 0

    def new_food(self):
        while True:
            position = Point(random.randint(1, self.width-2), random.randint(1, self.height-2))
            if position not in self.snake.body:
                return position

    def update(self):
        head = self.snake.body[0]
        if self.snake.direction == 'UP':
            new_head = Point(head.x, head.y-1)
        elif self.snake.direction == 'DOWN':
            new_head = Point(head.x, head.y+1)
        elif self.snake.direction == 'LEFT':
            new_head = Point(head.x-1, head.y)
        else:  # self.snake.direction == 'RIGHT'
            new_head = Point(head.x+1, head.y)

        if (new_head.x in [0, self.width] or
            new_head.y in [0, self.height] or
            new_head in self.snake.body):
            self.snake.alive = False
        else:
            self.snake.body.insert(0, new_head)
            if new_head == self.food:
                self.score += 1
                self.food = self.new_food()
            else:
                self.snake.body.pop()

    def draw(self):
        self.screen.clear()
        for y in range(self.height):
            for x in range(self.width):
                point = Point(x, y)
                if point == self.snake.body[0]:
                    self.screen.addch(y, x, 'O')
                elif point in self.snake.body:
                    self.screen.addch(y, x, 'o')
                elif point == self.food:
                    self.screen.addch(y, x, '*')
                elif x in [0, self.width-1] or y in [0, self.height-1]:
                    self.screen.addch(y, x, '#')
        self.screen.refresh()

    def handle_input(self):
        key = self.screen.getch()
        if key in [curses.KEY_UP, ord('w')] and self.snake.direction != 'DOWN':
            self.snake.direction = 'UP'
        elif key in [curses.KEY_DOWN, ord('s')] and self.snake.direction != 'UP':
            self.snake.direction = 'DOWN'
        elif key in [curses.KEY_LEFT, ord('a')] and self.snake.direction != 'RIGHT':
            self.snake.direction = 'LEFT'
        elif key in [curses.KEY_RIGHT, ord('d')] and self.snake.direction != 'LEFT':
            self.snake.direction = 'RIGHT'

    def run(self):
        while self.snake.alive:
            self.draw()
            self.handle_input()
            self.update()
            self.screen.timeout(100 - min(90, self.score))

def main():
    curses.initscr()
    curses.curs_set(0)
    screen = curses.newwin(20, 60, 0, 0)
    screen.keypad(1)
    screen.timeout(100)
    game = Game(screen)
    game.run()
    curses.endwin()

if __name__ == '__main__':
    main()
