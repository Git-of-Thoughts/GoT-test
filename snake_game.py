import random
import curses

class Snake:
    def __init__(self, window, start_pos):
        self.body = [start_pos]
        self.window = window

    def move(self, direction):
        # Move the snake in the given direction
        head = self.body[0]
        new_head = (head[0] + direction[0], head[1] + direction[1])
        self.body.insert(0, new_head)

    def grow(self):
        # Add a new segment to the snake's body
        self.body.append(self.body[-1])

    def collided_with_self(self):
        # Check if the snake has collided with itself
        return self.body[0] in self.body[1:]

class Food:
    def __init__(self, window, snake):
        self.window = window
        self.snake = snake
        self.pos = self.place_food()

    def place_food(self):
        # Place the food at a random location on the game board
        while True:
            pos = (random.randint(0, self.window.getmaxyx()[0]-1), random.randint(0, self.window.getmaxyx()[1]-1))
            if pos not in self.snake.body:
                return pos

class Game:
    def __init__(self, window):
        self.window = window
        self.snake = Snake(window, (10, 10))
        self.food = Food(window, self.snake)
        self.score = 0

    def start(self):
        # Start the game
        while True:
            self.window.clear()
            self.window.addstr(0, 0, f'Score: {self.score}')
            self.window.addch(self.food.pos[0], self.food.pos[1], '#')
            for segment in self.snake.body:
                self.window.addch(segment[0], segment[1], '*')
            self.window.refresh()

            key = self.window.getch()
            if key == curses.KEY_UP:
                self.snake.move((-1, 0))
            elif key == curses.KEY_DOWN:
                self.snake.move((1, 0))
            elif key == curses.KEY_LEFT:
                self.snake.move((0, -1))
            elif key == curses.KEY_RIGHT:
                self.snake.move((0, 1))

            if self.snake.body[0] == self.food.pos:
                self.score += 1
                self.snake.grow()
                self.food = Food(self.window, self.snake)
            elif self.snake.collided_with_self():
                break

def main():
    curses.initscr()
    window = curses.newwin(20, 60, 0, 0)
    window.keypad(1)
    window.timeout(100)
    game = Game(window)
    game.start()
    curses.endwin()

if __name__ == "__main__":
    main()
