class BinaryWord:
    def __init__(self, word):
        self.word = word

    def validate(self):
        if not all(c in '01' for c in self.word):
            raise ValueError(f"{self.word} is not a valid binary word")

    def count_zeros(self):
        return self.word.count('0')

    def count_ones(self):
        return self.word.count('1')
