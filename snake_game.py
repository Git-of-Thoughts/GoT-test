import random
import os
import msvcrt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self, init_body, direction):
        self.body = init_body
        self.direction = direction

    def move(self):
        head = self.body[0]
        if self.direction == 'up':
            new_head = Point(head.x, head.y - 1)
        elif self.direction == 'down':
            new_head = Point(head.x, head.y + 1)
        elif self.direction == 'left':
            new_head = Point(head.x - 1, head.y)
        else:  # self.direction == 'right'
            new_head = Point(head.x + 1, head.y)
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        tail = self.body[-1]
        self.body.append(tail)

    def self_collision(self):
        head = self.body[0]
        return any(body_part.x == head.x and body_part.y == head.y for body_part in self.body[1:])

class Game:
    def __init__(self, grid_size, snake, food):
        self.grid_size = grid_size
        self.snake = snake
        self.food = food
        self.score = 0

    def draw_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if any(point.x == j and point.y == i for point in self.snake.body):
                    print('S', end='')
                elif self.food.x == j and self.food.y == i:
                    print('F', end='')
                else:
                    print('.', end='')
            print()

    def generate_food(self):
        while True:
            x = random.randint(0, self.grid_size - 1)
            y = random.randint(0, self.grid_size - 1)
            if all(point.x != x or point.y != y for point in self.snake.body):
                return Point(x, y)

    def handle_input(self):
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()
            if key == 'w' and self.snake.direction != 'down':
                self.snake.direction = 'up'
            elif key == 's' and self.snake.direction != 'up':
                self.snake.direction = 'down'
            elif key == 'a' and self.snake.direction != 'right':
                self.snake.direction = 'left'
            elif key == 'd' and self.snake.direction != 'left':
                self.snake.direction = 'right'

    def game_over(self):
        head = self.snake.body[0]
        return (head.x < 0 or head.y < 0 or head.x >= self.grid_size or head.y >= self.grid_size or
                self.snake.self_collision())

    def play(self):
        while True:
            os.system('cls')
            self.draw_grid()
            self.handle_input()
            if self.game_over():
                print('Game Over! Your score is: ', self.score)
                break
            head = self.snake.body[0]
            if head.x == self.food.x and head.y == self.food.y:
                self.score += 1
                self.snake.grow()
                self.food = self.generate_food()
            else:
                self.snake.move()

if __name__ == '__main__':
    snake = Snake([Point(5, 5)], 'right')
    game = Game(10, snake, Point(7, 7))
    game.play()
