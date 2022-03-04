# Creates the playlists 
# To create a playlist for a user, Scopes have to be defined for the accesstoken.
# json.dumps(current_user, indent = 2)


from spotipy import SpotifyClientCredentials
import accesstoken
import json
import os
import spotipy 
from recommender import Recommender as rec

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
    
    # successfully creates a playlist IMMA CRYYYY FOR REALLLLL
    def add_playlist(self, pl_name:str, mood:list, energy:float, valence:float):
        create = sp.user_playlist_create(Playlists.get_user_id(), pl_name)
        moods = rec.random_selector(self,list= mood)
        mood_songs = rec.mood_recommender(self , mood = moods, energy = energy, valence = valence)
        playlist_id = str(create['id'])
        songs_id = rec.get_song_id_list(self, tracks = mood_songs)
        added_playlist = sp.playlist_add_items(playlist_id, songs_id)
        return added_playlist

playlists = Playlists()
print(playlists.add_playlist(pl_name = 'First Musynq playlist ever', 
                                mood = rec.Happy,
                                energy = 0.7,
                                valence = 0.8))