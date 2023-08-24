class Screen:
    def __init__(self):
        self.score = 0

    def display(self, snake, food):
        for i in range(20):
            for j in range(20):
                if (i, j) in snake.body:
                    print("S", end="")
                elif (i, j) == food.position:
                    print("F", end="")
                else:
                    print(".", end="")
            print()
        print(f"Score: {self.score}")

    def increment_score(self):
        self.score += 1
