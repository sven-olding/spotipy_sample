import spotipy
import random
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id='318cf83051e84ed1baa0d95770436429', client_secret='1896cc0272434bacab41ba8345f82129')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

category_playlists = sp.category_playlists(category_id="workout", country="DE", limit=50)

# Playlists der Kategorie Workout ausgeben
for playlist in category_playlists['playlists']['items']:
  print(playlist['name'])  
  print("-" * 30)


# Zufällige Playlist der Kategorie
random_playlist = random.choice(category_playlists['playlists']['items'])
print(f"Zufällige Auswahl: {random_playlist['name']}")