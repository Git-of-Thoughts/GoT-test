import curses
from direction import Direction
from snake import Snake
from food import Food
from point import Point

class Game:
    def __init__(self, game_width, game_height):
        self.game_width = game_width
        self.game_height = game_height
        self.snake = Snake(Point(game_width // 2, game_height // 2))
        self.food = Food(game_width, game_height)
        self.score = 0

    def game_loop(self, window):
        while True:
            self.snake.move()
            if self.snake.get_head() == self.food.position:
                self.snake.grow()
                self.score += 1
                self.food = Food(self.game_width, self.game_height)
            elif (self.snake.get_head().x < 0 or self.snake.get_head().y < 0 or
                  self.snake.get_head().x >= self.game_width or self.snake.get_head().y >= self.game_height or
                  self.snake.collided_with_self()):
                break
            self.draw(window)

    def draw(self, window):
        window.clear()
        for part in self.snake.body:
            window.addch(part.y, part.x, '#')
        window.addch(self.food.position.y, self.food.position.x, '*')
        window.addstr(0, 0, 'Score: ' + str(self.score))

    def start(self):
        curses.wrapper(self.game_loop)
