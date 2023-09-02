import random
from snake import Snake
from food import Food
from point import Point

class Game:
    def __init__(self, board_size):
        self.board_size = board_size
        self.snake = Snake(Point(board_size // 2, board_size // 2))
        self.food = Food(board_size)

    def game_loop(self):
        while True:
            self.snake.move()
            if self.snake.head() == self.food.position:
                self.snake.grow()
                self.food = Food(self.board_size)
            elif (self.snake.self_collision() or
                  not self.snake.in_bounds(self.board_size)):
                break
            self.draw_board()

    def draw_board(self):
        for i in range(self.board_size):
            for j in range(self.board_size):
                point = Point(i, j)
                if self.snake.on_body(point):
                    print('S', end='')
                elif point == self.food.position:
                    print('F', end='')
                else:
                    print('.', end='')
            print()

if __name__ == "__main__":
    game = Game(10)
    game.game_loop()
