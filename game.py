import os
import time
import msvcrt
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0

    def run(self):
        while True:
            self.handle_input()
            self.update()
            self.draw()
            time.sleep(0.1)

    def handle_input(self):
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()
            if key == 'w' and self.snake.direction != 'down':
                self.snake.direction = 'up'
            elif key == 'a' and self.snake.direction != 'right':
                self.snake.direction = 'left'
            elif key == 's' and self.snake.direction != 'up':
                self.snake.direction = 'down'
            elif key == 'd' and self.snake.direction != 'left':
                self.snake.direction = 'right'

    def update(self):
        self.snake.move()
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.score += 1
            self.food.respawn()
        if self.snake.collides_with_self() or not (0 <= self.snake.body[0][0] < 20 and 0 <= self.snake.body[0][1] < 20):
            print('Game Over! Your score is: ', self.score)
            exit()

    def draw(self):
        os.system('cls')
        for i in range(20):
            for j in range(20):
                if (i, j) in self.snake.body:
                    print('S', end='')
                elif (i, j) == self.food.position:
                    print('F', end='')
                else:
                    print('.', end='')
            print()

if __name__ == '__main__':
    game = Game()
    game.run()
