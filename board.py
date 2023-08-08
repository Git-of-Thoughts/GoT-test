class Board:
    def __init__(self, width, height, snake, food):
        self.width = width
        self.height = height
        self.snake = snake
        self.food = food

    def draw(self):
        for i in range(self.height):
            for j in range(self.width):
                if (j, i) in self.snake.positions:
                    print('S', end='')
                elif (j, i) == self.food.position:
                    print('F', end='')
                else:
                    print('.', end='')
            print()
