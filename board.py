class Board:
    def __init__(self, snake, fruit):
        self.snake = snake
        self.fruit = fruit
        self.board = [[' ' for _ in range(20)] for _ in range(20)]

    def update(self):
        self.board = [[' ' for _ in range(20)] for _ in range(20)]
        for position in self.snake.positions:
            self.board[position[0]][position[1]] = 'S'
        self.board[self.fruit.position[0]][self.fruit.position[1]] = 'F'

    def print(self):
        for row in self.board:
            print(''.join(row))
