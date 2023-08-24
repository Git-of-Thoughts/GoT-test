class BinaryWordAnalyzer:
    def __init__(self, words):
        self.words = words

    def find_most_zeros(self):
        return max(self.words, key=lambda word: word.count_zeros())

    def find_most_ones(self):
        return max(self.words, key=lambda word: word.count_ones())
