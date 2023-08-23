import random
from snake import Snake
from apple import Apple

class Game:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.snake = Snake()
        self.apple = Apple(self.width, self.height)

    def start(self):
        while True:
            self.snake.move()
            if self.snake.head == self.apple.position:
                self.snake.grow()
                self.apple = Apple(self.width, self.height)
            elif (self.snake.head.x < 0 or self.snake.head.y < 0 or
                  self.snake.head.x >= self.width or self.snake.head.y >= self.height or
                  self.snake.head in self.snake.body):
                break
            self.render()

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.snake.head.x == x and self.snake.head.y == y:
                    print('S', end='')
                elif self.apple.position.x == x and self.apple.position.y == y:
                    print('A', end='')
                elif any(point.x == x and point.y == y for point in self.snake.body):
                    print('s', end='')
                else:
                    print('.', end='')
            print()

if __name__ == "__main__":
    Game().start()
