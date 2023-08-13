class Game:
    def __init__(self):
        self.score = 0

    def start(self):
        self.score = 0

    def tap(self):
        self.score += 1

    def end(self):
        return self.score
