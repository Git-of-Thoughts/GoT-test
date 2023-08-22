class Board:
    def __init__(self, snake, food):
        self.snake = snake
        self.food = food
        self.board = self.initialize_board()

    def initialize_board(self):
        board = [['.' for _ in range(20)] for _ in range(20)]
        for position in self.snake.positions:
            board[position[1]][position[0]] = 'S'
        board[self.food.position[1]][self.food.position[0]] = 'F'
        return board

    def update_board(self):
        self.board = self.initialize_board()

    def display_board(self):
        for row in self.board:
            print(' '.join(row))
