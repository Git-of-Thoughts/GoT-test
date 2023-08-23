import curses
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0

    def start(self):
        # Initialize the screen
        self.screen = curses.initscr()
        curses.curs_set(0)
        self.screen.keypad(1)
        self.screen.timeout(100)

        # Game loop
        while True:
            self.screen.clear()
            self.screen.addstr(str(self.score) + ' ')
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            self.screen.refresh()

            # Handle user input
            key = self.screen.getch()
            self.snake.change_direction(key)

            # Update game state
            if self.snake.move() == "COLLISION":
                break
            if self.snake.head == self.food.position:
                self.score += 1
                self.snake.grow()
                self.food = Food()

        # End the game
        curses.endwin()

