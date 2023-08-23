from point import Point

class Snake:
    def __init__(self):
        self.body = [Point(0, 0)]

    def get_head_position(self):
        return self.body[0]

    def update_position(self, direction):
        # Update the position of the snake based on the given direction

    def grow(self):
        # Add a new point to the body of the snake

    def check_collision(self):
        # Check if the snake has collided with itself
