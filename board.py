class Board:
    def __init__(self, size, snake, fruit):
        self.size = size
        self.snake = snake
        self.fruit = fruit

    def draw(self):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) in self.snake.body:
                    print("S", end="")
                elif (i, j) == self.fruit.position:
                    print("F", end="")
                else:
                    print(".", end="")
            print()

    def update(self):
        self.snake.move()
        if self.snake.body[0] == self.fruit.position:
            self.snake.grow()
            self.fruit = Fruit(self.size)
