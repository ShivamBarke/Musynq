# Creates the playlists 
# Under development
# json.dumps(current_user, indent = 2)


import spotipy
import os
from spotipy import SpotifyClientCredentials
import accesstoken
import json

os.environ["SPOTIPY_CLIENT_ID"] = "d04be567989d427e8ca8b0b27faa9bdc"
os.environ["SPOTIPY_CLIENT_SECRET"]= "07721eeec6e1493f80a52f79335f1a12"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://127.0.0.1:5500/index.html"

token = accesstoken.get_token()
auth_manager = spotipy.SpotifyClientCredentials()
sp = spotipy.Spotify(auth = token)

class Playlists:
    def get_user_id():
        current_user = sp.current_user()
        user_id = current_user['id']
        return user_id
    # successfully creates a playlist IMMA CRYYYY
    def create_playlist(self, pl_name):
        create = sp.user_playlist_create(Playlists.get_user_id(), pl_name)
        return create

pl = Playlists()
print(pl.create_playlist('trial'))