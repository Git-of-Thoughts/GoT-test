import random
import os
import time
import msvcrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def equals(self, other):
        return self.x == other.x and self.y == other.y

class Fruit:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.position = Point(0, 0)
        self.respawn()

    def respawn(self):
        self.position = Point(random.randint(0, self.width - 1), random.randint(0, self.height - 1))

class Snake:
    def __init__(self, x, y):
        self.body = [Point(x, y)]
        self.direction = 'UP'

    def move(self):
        head = self.get_head()
        if self.direction == 'UP':
            self.body.insert(0, Point(head.x, head.y - 1))
        elif self.direction == 'DOWN':
            self.body.insert(0, Point(head.x, head.y + 1))
        elif self.direction == 'LEFT':
            self.body.insert(0, Point(head.x - 1, head.y))
        elif self.direction == 'RIGHT':
            self.body.insert(0, Point(head.x + 1, head.y))
        self.body.pop()

    def grow(self):
        head = self.get_head()
        self.body.insert(0, Point(head.x, head.y))

    def get_head(self):
        return self.body[0]

    def collides_with_self(self):
        return self.get_head() in self.body[1:]

    def collides_with(self, point):
        return self.get_head().equals(point)

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = Snake(width // 2, height // 2)
        self.fruit = Fruit(width, height)
        self.score = 0
        self.is_running = True

    def run(self):
        while self.is_running:
            self.draw()
            self.handle_input()
            self.update()
            time.sleep(0.1)

    def end(self):
        self.is_running = False

    def draw(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(self.height):
            for x in range(self.width):
                point = Point(x, y)
                if self.snake.collides_with(point):
                    print('S', end='')
                elif self.fruit.position.equals(point):
                    print('F', end='')
                else:
                    print('.', end='')
            print()
        print(f'Score: {self.score}')

    def handle_input(self):
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()
            if key == 'w' and self.snake.direction != 'DOWN':
                self.snake.direction = 'UP'
            elif key == 's' and self.snake.direction != 'UP':
                self.snake.direction = 'DOWN'
            elif key == 'a' and self.snake.direction != 'RIGHT':
                self.snake.direction = 'LEFT'
            elif key == 'd' and self.snake.direction != 'LEFT':
                self.snake.direction = 'RIGHT'

    def update(self):
        self.snake.move()
        if self.snake.collides_with_self():
            self.end()
        elif self.snake.get_head().x < 0 or self.snake.get_head().x >= self.width or self.snake.get_head().y < 0 or self.snake.get_head().y >= self.height:
            self.end()
        elif self.snake.collides_with(self.fruit.position):
            self.snake.grow()
            self.fruit.respawn()
            self.score += 1

if __name__ == '__main__':
    game = Game(20, 20)
    game.run()
