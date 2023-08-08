from point import Point

class Snake:
    def __init__(self, board):
        self.board = board
        self.direction = Point(0, 1)
        self.body = [Point(board.height // 2, board.width // 2)]

    def change_direction(self, key):
        if key == curses.KEY_UP and self.direction.y != 1:
            self.direction = Point(-1, 0)
        elif key == curses.KEY_DOWN and self.direction.y != -1:
            self.direction = Point(1, 0)
        elif key == curses.KEY_LEFT and self.direction.x != 1:
            self.direction = Point(0, -1)
        elif key == curses.KEY_RIGHT and self.direction.x != -1:
            self.direction = Point(0, 1)

    def move(self):
        head = self.body[0]
        new_head = Point(head.y + self.direction.y, head.x + self.direction.x)

        if new_head in self.body or not self.board.is_valid_point(new_head):
            return False

        self.body.insert(0, new_head)

        if self.board.get_cell(new_head) != 'A':
            self.body.pop()
        else:
            return True

    def check_collision(self):
        head = self.body[0]
        return head in self.body[1:] or not self.board.is_valid_point(head)
