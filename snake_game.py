import enum
import random
import curses

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Direction(enum.Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Snake:
    def __init__(self, head, direction):
        self.body = [head]
        self.direction = direction

    def move(self):
        head = self.body[0]
        if self.direction == Direction.UP:
            self.body.insert(0, Point(head.x, head.y - 1))
        elif self.direction == Direction.DOWN:
            self.body.insert(0, Point(head.x, head.y + 1))
        elif self.direction == Direction.LEFT:
            self.body.insert(0, Point(head.x - 1, head.y))
        elif self.direction == Direction.RIGHT:
            self.body.insert(0, Point(head.x + 1, head.y))

    def eat(self):
        self.move()

    def die(self):
        self.body.pop()

class Food:
    def __init__(self, position):
        self.position = position

class Game:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.snake = Snake(Point(width // 2, height // 2), Direction.UP)
        self.food = Food(Point(random.randint(0, width - 1), random.randint(0, height - 1)))
        self.score = 0

    def draw(self):
        self.screen.clear()
        for part in self.snake.body:
            self.screen.addch(part.y, part.x, '#')
        self.screen.addch(self.food.position.y, self.food.position.x, '*')
        self.screen.addstr(0, 0, f'Score: {self.score}')

    def handle_input(self):
        key = self.screen.getch()
        if key == curses.KEY_UP and self.snake.direction != Direction.DOWN:
            self.snake.direction = Direction.UP
        elif key == curses.KEY_DOWN and self.snake.direction != Direction.UP:
            self.snake.direction = Direction.DOWN
        elif key == curses.KEY_LEFT and self.snake.direction != Direction.RIGHT:
            self.snake.direction = Direction.LEFT
        elif key == curses.KEY_RIGHT and self.snake.direction != Direction.LEFT:
            self.snake.direction = Direction.RIGHT

    def update(self):
        self.snake.move()
        if self.snake.body[0] == self.food.position:
            self.snake.eat()
            self.score += 1
            self.food = Food(Point(random.randint(0, self.width - 1), random.randint(0, self.height - 1)))
        else:
            self.snake.die()

    def check_collision(self):
        head = self.snake.body[0]
        if head.x < 0 or head.y < 0 or head.x >= self.width or head.y >= self.height or head in self.snake.body[1:]:
            return True
        return False

def game_loop(screen):
    curses.curs_set(0)
    screen.nodelay(1)
    width, height = screen.getmaxyx()
    game = Game(screen, width, height)
    while True:
        game.draw()
        game.handle_input()
        game.update()
        if game.check_collision():
            break

if __name__ == '__main__':
    curses.wrapper(game_loop)
