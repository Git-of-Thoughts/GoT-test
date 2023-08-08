import curses
from board import Board
from snake import Snake

class Game:
    def __init__(self):
        self.board = Board(20, 20)
        self.snake = Snake(self.board)
        self.score = 0

    def run(self):
        # Initialize curses
        stdscr = curses.initscr()
        curses.cbreak()
        stdscr.keypad(1)
        stdscr.timeout(100)

        while True:
            # Get user input
            key = stdscr.getch()
            self.snake.change_direction(key)

            # Update game state
            if self.snake.move():
                self.score += 1
                self.board.place_apple()

            # Draw game state
            self.board.draw(stdscr, self.snake, self.score)

            # Check game over condition
            if self.snake.check_collision():
                break

        # Clean up curses
        stdscr.keypad(0)
        curses.echo()
        curses.nocbreak()
        curses.endwin()