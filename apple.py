from point import Point

class Apple:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.position = Point(0, 0)
        self.generate_new_position()

    def generate_new_position(self):
        # Generate a new position for the apple
