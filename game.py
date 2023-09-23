import random
from snake import Snake
from food import Food
from position import Position

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        self.snake = Snake()
        self.food = Food(self.spawn_food())
        self.score = 0
        self.game_over = False

    def play(self):
        while not self.game_over:
            self.get_input()
            self.update()
            self.draw()

    def get_input(self):
        direction = input("Enter direction (w/a/s/d): ")
        self.snake.set_direction(direction)

    def update(self):
        if self.snake.move() == self.food.position:
            self.snake.grow()
            self.score += 1
            self.food = Food(self.spawn_food())
        elif self.check_collision():
            self.game_over = True

    def draw(self):
        for i in range(self.height):
            for j in range(self.width):
                if Position(j, i) == self.snake.head:
                    print("S", end="")
                elif Position(j, i) in self.snake.body:
                    print("s", end="")
                elif Position(j, i) == self.food.position:
                    print("F", end="")
                else:
                    print(".", end="")
            print()
        print(f"Score: {self.score}")

    def check_collision(self):
        return (self.snake.head in self.snake.body[1:] or
                not (0 <= self.snake.head.x < self.width and
                     0 <= self.snake.head.y < self.height))

    def spawn_food(self):
        while True:
            position = Position(random.randint(0, self.width - 1),
                                random.randint(0, self.height - 1))
            if position not in self.snake.body:
                return position
