from .snake import Snake

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = Snake()
        self.item = self.generate_item()

    def generate_item(self):
        # Generate a random item within the game grid
        pass

    def update(self):
        self.snake.move()
        if self.snake.collides_with_self():
            return 'game over'
        elif self.snake.collides_with_item(self.item):
            self.snake.grow()
            self.item = self.generate_item()
        return 'continue'

    def change_snake_direction(self, direction):
        self.snake.change_direction(direction)
