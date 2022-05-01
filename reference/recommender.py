# this file recommends songs based on the mood. 
# Needs Code optimisation in making one function for mood_recommender() instead of having to make 4 different functions.

import os
import random

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from . import accesstoken

os.environ["SPOTIPY_CLIENT_ID"] = "d04be567989d427e8ca8b0b27faa9bdc"
os.environ["SPOTIPY_CLIENT_SECRET"]= "66c4769463364b50b88804f7013c95df"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:3000/"

token = accesstoken.get_token()
sp = spotipy.Spotify(auth = token)
auth_manager = spotipy.SpotifyClientCredentials()

song_name_list = []
song_id_list = []

class Recommender():
    # Selects random song genres from above defined lists i.e happy sad angry relax
    # Add duration specific songs duration > 1 min
    song_name_list = []
    song_id_list = []
    Happy = ['hip hop', 'classical',' edm' ,'blues', 'country', 'funk', 'disco','love songs',' latino',' dubstep', 'punk', 'punk-rock' , 
            'heavy metal' , 'rock', 'rock-n-roll' ,'party','synth-pop', 'salsa', 'samba' ,'guitar', 'happy','alt-rock','indie', 'indie-pop','trance']

    Sad = ['classical', 'broadway', 'blues','chill','sad','club', 'comedy']

    Relaxed= ['classical' , 'new age', 'love songs', 'jazz',' latino', ' chill',' work-out','road-trip', 'opera', 'sleep','acoustic','hip-hop', 'holidays','movies','trance','drum-and-bass','new-age','club', 'comedy']

    Anger= ['reggae' ,'club', 'death -metal','drum-and-bass',' dub', 'dubstep', 'edm', 'electro', 'electronic', 'emo','heavy metal','alt-rock','drum-and-bass']
    
    Mood = [Happy, Sad, Anger, Relaxed]
    def random_selector(self , list: list) :
        for i in range(5):
            list1 = random.choices(list, k=5)
        return list1   
    
    def get_song_name_list(self , tracks): 
        for i in range(10):
            song_name = tracks[i]['name']
            Recommender.song_name_list.append(song_name)
        return Recommender.song_name_list

    def get_song_id_list(self, tracks):
        for i in range(10):
            song_id = tracks[i]['id']
            Recommender.song_id_list.append(song_id)
        return Recommender.song_id_list

    # Recommends MOOD wise playlists using spotipy library

    def mood_recommender(self, mood:list, energy:float, valence:float):
        recommend = sp.recommendations(
            seed_genres = mood,
            limit = 10,
            country = 'IN',
            target_energy = energy,
            target_valence = valence,
            min_popularity = 45
        )
        return recommend.get('tracks')

# # Sample for calling the recommender function.        
# rec = Recommender()
# # happy = list(rec.Happy)

# # gets random 5 playlists from the available playlist categorised in the Happy, Sad etc.
# mood = rec.random_selector(rec.Happy)

# # generated mood wise songs using moodtracks, energy, valence as parameters
# happy_tracks= list(rec.mood_recommender(mood, 0.7, 0.6))


# mood_song_id_info = rec.get_song_id_list(happy_tracks)

# # print(mood_song_id_info)
