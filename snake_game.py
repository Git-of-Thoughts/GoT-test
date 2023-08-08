import random
import os
import time

class Game:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.reset()

    def reset(self):
        self.board = [[' ']*self.width for _ in range(self.height)]
        self.snake = Snake(self.width//2, self.height//2)
        self.place_apple()
        self.score = 0

    def draw_board(self):
        os.system('clear')
        print('-'*(self.width+2))
        for row in self.board:
            print('|' + ''.join(row) + '|')
        print('-'*(self.width+2))
        print('Score: ', self.score)

    def place_apple(self):
        while True:
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            if self.board[y][x] == ' ':
                self.board[y][x] = '*'
                break

    def game_over(self):
        x, y = self.snake.get_head()
        return x < 0 or y < 0 or x >= self.width or y >= self.height or (x, y) in self.snake.get_body()

    def run(self):
        while True:
            self.draw_board()
            time.sleep(0.1)
            self.snake.move()
            if self.game_over():
                print('Game Over!')
                break
            x, y = self.snake.get_head()
            if self.board[y][x] == '*':
                self.score += 1
                self.snake.grow()
                self.place_apple()
            self.board = [[' ']*self.width for _ in range(self.height)]
            self.board[y][x] = 'O'
            for x, y in self.snake.get_body():
                self.board[y][x] = 'o'

class Snake:
    DIRECTIONS = {'UP': (0, -1), 'DOWN': (0, 1), 'LEFT': (-1, 0), 'RIGHT': (1, 0)}

    def __init__(self, x, y):
        self.body = [(x, y)]
        self.direction = self.DIRECTIONS['UP']

    def move(self):
        x, y = self.body[0]
        dx, dy = self.direction
        self.body.insert(0, (x+dx, y+dy))
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def change_direction(self, direction):
        self.direction = self.DIRECTIONS[direction]

    def get_head(self):
        return self.body[0]

    def get_body(self):
        return self.body[1:]

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
