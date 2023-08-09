import random
from snake import Snake
from food import Food

class Game:
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.snake = Snake()
        self.food = Food(self.grid_size)

    def draw_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if (i, j) in self.snake.body:
                    print('S', end='')
                elif (i, j) == self.food.position:
                    print('F', end='')
                else:
                    print('.', end='')
            print()

    def play(self):
        while True:
            self.draw_grid()
            direction = input('Enter direction (up, down, left, right): ')
            if direction not in ['up', 'down', 'left', 'right']:
                continue
            if not self.snake.move(direction):
                break
            if self.snake.head == self.food.position:
                self.snake.grow()
                self.food = Food(self.grid_size)
        print('Game over!')

if __name__ == '__main__':
    game = Game(10)
    game.play()
