class Game:
    def __init__(self):
        pygame.init()
        self.snake = Snake()
        self.food = Food()

    def draw(self):
        self.snake.draw(self.surface)
        self.food.draw(self.surface)

    def update(self):
        self.snake.move()
        if self.snake.get_head_position() == self.food.position:
            self.snake.length += 1
            self.food.randomize_position()

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.turn(UP)
                    elif event.key == pygame.K_DOWN:
                        self.snake.turn(DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.snake.turn(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.turn(RIGHT)
            self.surface.fill((0,0,0))
            self.draw()
            self.update()
            pygame.display.update()
            clock.tick(12)
