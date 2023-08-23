class Game:
    def __init__(self):
        pygame.init()
        self.snake = Snake()
        self.food = Food()

    def check_for_collision(self):
        if self.snake.get_head_position() == self.food.position:
            self.snake.length += 1
            self.food.randomize_position()

    def run(self):
        clock = pygame.time.Clock()
        surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

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

            self.snake.move()
            self.check_for_collision()

            surface.fill((0,0,0)) # Background color
            self.snake.draw(surface)
            self.food.draw(surface)
            screen.blit(surface, (0,0))

            pygame.display.update()
            clock.tick(10) # Game speed
