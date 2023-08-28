import curses
from game import Game

def main(stdscr):
    curses.curs_set(0)
    window = curses.newwin(20, 60, 0, 0)
    window.keypad(1)
    window.timeout(100)
    game = Game(window)
    game.start()

if __name__ == "__main__":
    curses.wrapper(main)
