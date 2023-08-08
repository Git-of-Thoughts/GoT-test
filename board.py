import random
from point import Point

class Board:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.cells = [[' ' for _ in range(width)] for _ in range(height)]
        self.place_apple()

    def place_apple(self):
        while True:
            y = random.randint(0, self.height - 1)
            x = random.randint(0, self.width - 1)
            if self.cells[y][x] == ' ':
                self.cells[y][x] = 'A'
                break

    def get_cell(self, point):
        return self.cells[point.y][point.x]

    def is_valid_point(self, point):
        return 0 <= point.y < self.height and 0 <= point.x < self.width

    def draw(self, stdscr, snake, score):
        stdscr.clear()
        for y in range(self.height):
            for x in range(self.width):
                char = self.cells[y][x]
                if Point(y, x) in snake.body:
                    char = 'S'
                stdscr.addch(y, x, char)
        stdscr.addstr(self.height, 0, f'Score: {score}')
        stdscr.refresh()
