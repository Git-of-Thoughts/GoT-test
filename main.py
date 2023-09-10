import curses
from game import Game

def main(screen):
    game = Game(screen)
    game.play()

if __name__ == "__main__":
    curses.wrapper(main)
