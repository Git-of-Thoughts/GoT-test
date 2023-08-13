from collections import defaultdict

class CountryRanking:
    def __init__(self):
        self.scores = defaultdict(int)

    def add_score(self, country, score):
        self.scores[country] += score

    def get_ranking(self):
        return sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
