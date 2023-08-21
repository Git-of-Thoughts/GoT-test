class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()

    def is_collision(self):
        if self.snake.get_head_position() in self.snake.positions[1:]:
            return True
        return False

    def update(self):
        self.snake.move()
        if self.is_collision():
            self.snake.reset()
        elif self.snake.get_head_position() == self.food.position:
            self.snake.length += 1
            self.food.randomize_position()

    def draw(self, surface):
        self.snake.draw(surface)
        self.food.draw(surface)
