def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    game.snake.turn(UP)
                elif event.key == K_DOWN:
                    game.snake.turn(DOWN)
                elif event.key == K_LEFT:
                    game.snake.turn(LEFT)
                elif event.key == K_RIGHT:
                    game.snake.turn(RIGHT)

        game.snake.move()
        game.is_collision()
        game.draw(surface)
        screen.blit(surface, (0,0))
        pygame.display.update()
        clock.tick(8)

if __name__ == "__main__":
    main()
