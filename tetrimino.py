from point import Point

class Tetrimino:
    SHAPES = [
        [(0, 0), (1, 0), (2, 0), (3, 0)],  # I
        [(0, 0), (1, 0), (2, 0), (1, 1)],  # T
        [(0, 0), (1, 0), (0, 1), (1, 1)],  # O
        [(0, 0), (1, 0), (1, 1), (2, 1)],  # Z
        [(1, 0), (0, 1), (1, 1), (2, 0)],  # S
        [(0, 0), (1, 0), (2, 0), (2, 1)],  # L
        [(2, 0), (0, 1), (1, 1), (2, 1)]   # J
    ]

    def __init__(self, shape):
        self.points = [Point(x, y) for x, y in shape]
