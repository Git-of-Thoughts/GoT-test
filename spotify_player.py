import spotipy
from spotipy.oauth2 import SpotifyOAuth

class SpotifyPlayer:
    def __init__(self, client_id, client_secret, redirect_uri, scope):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                                            client_secret=client_secret,
                                                            redirect_uri=redirect_uri,
                                                            scope=scope))

    def get_random_song(self, playlist_id):
        results = self.sp.playlist(playlist_id)
        songs = results['tracks']['items']
        song = random.choice(songs)
        return song['track']['uri']

    def play_song(self, song_uri):
        self.sp.start_playback(uris=[song_uri])
