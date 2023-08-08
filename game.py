from snake import Snake
from food import Food

class Game:
    def __init__(self, board_size):
        self.board_size = board_size
        self.snake = Snake()
        self.food = Food(board_size)

    def is_game_over(self):
        head = self.snake.get_head()
        return (head in self.snake.get_body()) or (head[0] < 0 or head[0] >= self.board_size or head[1] < 0 or head[1] >= self.board_size)

    def update(self, direction):
        self.snake.change_direction(direction)
        self.snake.move()
        if self.snake.get_head() == self.food.get_position():
            self.snake.length += 1
            self.food = Food(self.board_size)
