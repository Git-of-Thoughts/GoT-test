class Game:
    def __init__(self):
        pygame.init()
        self.snake = Snake()
        self.food = Food()

    def check_for_collision(self):
        if self.snake.get_head_position() == self.food.position:
            self.snake.length += 1
            self.food.randomize_position()

    def update(self):
        self.snake.move()
        self.check_for_collision()

    def draw(self, surface):
        self.snake.draw(surface)
        self.food.draw(surface)

    def is_over(self):
        if self.snake.get_head_position() in self.snake.positions[1:]:
            return True
        return False
