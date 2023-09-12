from point import Point

class Board:
    WIDTH = 10
    HEIGHT = 20

    def __init__(self):
        self.grid = [[0 for _ in range(Board.WIDTH)] for _ in range(Board.HEIGHT)]

    def add_tetrimino(self, tetrimino):
        for point in tetrimino.points:
            self.grid[point.y][point.x] = 1

    def is_collision(self, tetrimino):
        for point in tetrimino.points:
            if point.y < 0 or point.y >= Board.HEIGHT or point.x < 0 or point.x >= Board.WIDTH or self.grid[point.y][point.x] == 1:
                return True
        return False

    def move_down(self, tetrimino):
        for point in tetrimino.points:
            point.y += 1

    def clear_lines(self):
        full_lines = [i for i, row in enumerate(self.grid) if all(cell == 1 for cell in row)]
        for line in full_lines:
            del self.grid[line]
            self.grid.insert(0, [0 for _ in range(Board.WIDTH)])
        return len(full_lines)
