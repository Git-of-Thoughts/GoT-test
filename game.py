class Game:
    def __init__(self):
        pygame.init()
        self.snake = Snake()
        self.apple = Apple()

    def check_for_collision(self):
        if self.snake.get_head_position() == self.apple.position:
            self.snake.length += 1
            self.apple.randomize_position()

    def update(self):
        self.snake.move()
        self.check_for_collision()

    def draw(self, surface):
        self.snake.draw(surface)
        self.apple.draw(surface)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.turn(UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.turn(RIGHT)

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.update()
            pygame.time.Clock().tick(10)
