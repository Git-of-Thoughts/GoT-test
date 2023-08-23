import curses
from game import Game

def main(screen):
    game = Game(screen)
    game.run()

if __name__ == '__main__':
    curses.wrapper(main)
