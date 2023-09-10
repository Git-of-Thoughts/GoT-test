import random

class Game:
    def __init__(self, size=8):
        self.size = size
        self.board = self.create_board()

    def create_board(self):
        return [[Candy() for _ in range(self.size)] for _ in range(self.size)]

    def draw_board(self):
        for row in self.board:
            print(' '.join(str(candy) for candy in row))
        print()

    def swap(self, pos1, pos2):
        self.board[pos1[0]][pos1[1]], self.board[pos2[0]][pos2[1]] = self.board[pos2[0]][pos2[1]], self.board[pos1[0]][pos1[1]]

    def find_matches(self):
        # This is a simplified version of match finding. It only checks for matches in rows.
        matches = []
        for row in self.board:
            for i in range(self.size - 2):
                if row[i] == row[i+1] == row[i+2]:
                    matches.append((row[i], row[i+1], row[i+2]))
        return matches

    def remove_matches(self, matches):
        for match in matches:
            for candy in match:
                self.board[candy.row][candy.col] = None

    def fill_board(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.board[row][col] is None:
                    self.board[row][col] = Candy()

    def play(self):
        while True:
            self.draw_board()
            pos1 = input("Enter the position of the first candy to swap (row col): ")
            pos2 = input("Enter the position of the second candy to swap (row col): ")
            self.swap(pos1, pos2)
            matches = self.find_matches()
            self.remove_matches(matches)
            self.fill_board()

class Candy:
    def __init__(self):
        self.type = random.choice(['red', 'blue', 'green', 'yellow'])

    def __str__(self):
        return self.type[0]
