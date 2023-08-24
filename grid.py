class Grid:
    def __init__(self, size):
        self.size = size

    def draw(self, snake, food):
        for i in range(self.size):
            for j in range(self.size):
                if (i, j) in snake.body:
                    print("S", end="")
                elif (i, j) == food:
                    print("F", end="")
                else:
                    print(".", end="")
            print()
        print()
