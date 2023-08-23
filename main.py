import curses
from game import Game

def main(stdscr):
    # Initialize the game
    game = Game(stdscr)
    # Start the game
    game.start()

if __name__ == "__main__":
    curses.wrapper(main)
