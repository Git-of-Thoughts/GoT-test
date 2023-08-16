from player import Player
from room import Room

class Game:
    def __init__(self):
        self.player = Player()
        self.rooms = self.create_rooms()
        self.current_room = self.rooms[0]

    def create_rooms(self):
        # Create rooms here
        pass

    def game_loop(self):
        # Handle game loop here
        pass

if __name__ == "__main__":
    game = Game()
    game.game_loop()
