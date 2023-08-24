import time
from snake import Snake
from food import Food
from screen import Screen

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.screen = Screen()
        self.food.place(self.snake.body)

    def game_loop(self):
        while True:
            self.screen.display(self.snake, self.food)
            self.snake.move()
            if self.snake.get_head() == self.food.position:
                self.snake.grow()
                self.screen.increment_score()
                self.food.place(self.snake.body)
            if self.snake.has_collided_with_self():
                break
            time.sleep(0.1)

if __name__ == "__main__":
    game = Game()
    game.game_loop()
