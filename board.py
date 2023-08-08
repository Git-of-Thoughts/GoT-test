class Board:
    def __init__(self, size):
        self.size = size

    def draw(self, snake, apple):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) in snake.body:
                    print("S", end="")
                elif (i, j) == apple.position:
                    print("A", end="")
                else:
                    print(".", end="")
            print()

    def check_collision(self, snake):
        if snake.head in snake.body[1:] or \
           not (0 <= snake.head[0] < self.size and 0 <= snake.head[1] < self.size):
            return True
        return False
