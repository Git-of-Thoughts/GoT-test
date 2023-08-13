from game import Game
from spotify_player import SpotifyPlayer

def main():
    game = Game()
    player = SpotifyPlayer(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    game.snake.turn(UP)
                elif event.key == K_DOWN:
                    game.snake.turn(DOWN)
                elif event.key == K_LEFT:
                    game.snake.turn(LEFT)
                elif event.key == K_RIGHT:
                    game.snake.turn(RIGHT)

        game.update()
        if game.is_over():
            break

        song_uri = player.get_random_song(PLAYLIST_ID)
        player.play_song(song_uri)

        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == "__main__":
    main()
