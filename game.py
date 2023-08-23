class Game:
    def __init__(self):
        pygame.init()
        self.snake = Snake()
        self.food = Food()

    def update(self):
        self.snake.move()
        if self.snake.get_head_position() == self.food.position:
            self.snake.length += 1
            self.food.randomize_position()

    def draw(self, surface):
        surface.fill((0, 0, 0))
        self.snake.draw(surface)
        self.food.draw(surface)
        pygame.display.update()

    def run(self):
        clock = pygame.time.Clock()
        surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.update()
            self.draw(surface)
            clock.tick(60)
