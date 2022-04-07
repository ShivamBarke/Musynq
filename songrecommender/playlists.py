# Creates the playlists 
# To create a playlist for a user, Scopes have to be defined for the accesstoken.
# json.dumps(current_user, indent = 2)
# DO NOT FUCKING DARE TO TOUCH THIS

from spotipy import SpotifyClientCredentials
import accesstoken
import json
import os
import spotipy 
from recommender import Recommender as rec

os.environ["SPOTIPY_CLIENT_ID"] = "d04be567989d427e8ca8b0b27faa9bdc"
os.environ["SPOTIPY_CLIENT_SECRET"]= "66c4769463364b50b88804f7013c95df"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://127.0.0.1:5500/index.html"

token = accesstoken.get_token()
auth_manager = spotipy.SpotifyClientCredentials()
sp = spotipy.Spotify(auth = token)

class Playlists:
    def get_user_id():
        current_user = sp.current_user()
        user_id = current_user['id']
        return user_id

    # def create_playlist(self, pl_name):
    #     create = sp.user_playlist_create(Playlists.get_user_id(), pl_name)
    #     return create

    # def get_playlist():
        
    #     pass
    # successfully creates a playlist IMMA CRYYYY FOR REALLLLL
    def add_playlist(self, pl_name:str, mood:list, energy:float, valence:float):
        create = sp.user_playlist_create(Playlists.get_user_id(), pl_name)
        moods = rec.random_selector(self,list= mood)
        mood_songs = rec.mood_recommender(self , mood = moods, energy = energy, valence = valence)
        playlist_id = str(create['id'])
        songs_id = rec.get_song_id_list(self, tracks = mood_songs)
        added_playlist = sp.playlist_add_items(playlist_id, songs_id)
        return added_playlist

pl = Playlists()
print(pl.add_playlist(pl_name = 'playlist name take as input', 
                                mood = rec.Sad,
                                energy = 0.6,   
                                valence = 0.4))