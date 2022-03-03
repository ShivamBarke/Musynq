# Creates the playlists 
# Under development

from threading import currentThread
import spotipy
import os
from spotipy import SpotifyClientCredentials

os.environ["SPOTIPY_CLIENT_ID"] = "d04be567989d427e8ca8b0b27faa9bdc"
os.environ["SPOTIPY_CLIENT_SECRET"]= "07721eeec6e1493f80a52f79335f1a12"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://127.0.0.1:5500/index.html"

auth_manager = spotipy.SpotifyClientCredentials()
sp = spotipy.Spotify()

class Playlists:
    def create_playlist(self):
        current_user = sp.current_user()
        sp.user_playlist_create()
        return current_user

pl = Playlists()
print(pl.create_playlist())