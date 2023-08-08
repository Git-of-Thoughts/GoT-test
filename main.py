import pygame
from game import Game

def main():
    pygame.init()

    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        game.update()
        game.draw()

        pygame.display.flip()

if __name__ == "__main__":
    main()
