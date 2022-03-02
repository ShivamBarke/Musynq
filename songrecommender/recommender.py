# this file recommends songs based on the mood. 
# Needs Code optimisation in making one function for mood_recommender() instead of having to make 4 different functions.

import spotipy
import os
import random
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

os.environ["SPOTIPY_CLIENT_ID"] = "d04be567989d427e8ca8b0b27faa9bdc"
os.environ["SPOTIPY_CLIENT_SECRET"]= "07721eeec6e1493f80a52f79335f1a12"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://127.0.0.1:8000/index.html"

username = ''
token = util.prompt_for_user_token(username)

try : 
    token = util.prompt_for_user_token(username)
except :
    os.remove(f'.cache-{username}')
    token = util.prompt_for_user_token(username)

sp = spotipy.Spotify(auth= token)
auth_manager = spotipy.SpotifyClientCredentials()

Happy = ['hip hop', 'classical',' edm' ,'blues', 'country', 'funk', 'disco','love songs',' latino',' dubstep', 'punk', 'punk-rock' , 
 'heavy metal' , 'rock', 'rock-n-roll' ,'party','synth-pop', 'salsa', 'samba' ,'guitar', 'happy','alt-rock','indie', 'indie-pop','trance']

Sad = ['classical', 'broadway', 'blues','chill','sad','club', 'comedy']

Relaxed= ['classical' , 'new age', 'love songs', 'jazz',' latino', ' chill',' work-out','road-trip', 'opera', 'sleep','acoustic','hip-hop', 'holidays','movies','trance','drum-and-bass','new-age','club', 'comedy']

Anger= ['reggae' ,'club', 'death -metal','drum-and-bass',' dub', 'dubstep', 'edm', 'electro', 'electronic', 'emo','heavy metal','alt-rock','drum-and-bass']


class Recommender():
    # Selects random song genres from above defined lists i.e happy sad angry relax

    # Add duration specific songs duration > 1 min

    song_name_list = []
    song_id_list = []
    
    def __init__(self) -> None:
        song_name_list = []
        song_id_list = []
    
        self.song_name_list = song_name_list
        self.song_id_list = song_id_list
        
    def random_selector(list) :
        for i in range(5):
            list1 = random.choices(list, k=5)
        return list1   
    
    def get_song_name_list(self, tracks): 
        for i in range(10):
            song_name = tracks[i]['name']
            Recommender.song_name_list.append(song_name)
        return Recommender.song_name_list

    def get_song_id_list(self, tracks):
        for i in range(10):
            song_id = tracks[i]['id']
        return Recommender.song_id_list

    # Recommends MOOD wise playlists using spotipy library

    # def mood_recommender(self, mood, energy, valence):
    #     recommend = sp.recommendations(
    #         seed_genres = Recommender.random_selector(mood),
    #         limit = 10,
    #         country = 'IN',
    #         target_energy = energy,
    #         target_valence = valence,
    #         min_popularity = 45
    #     )
    #     return recommend.get('tracks')


    def happy_recommender(self):
        
        recommend = sp.recommendations(
            seed_genres = Recommender.random_selector(Happy),
            limit = 10,
            country = 'IN',
            min_energy = 0.5,
            min_valence = 0.5,
            min_popularity = 30
        )
        return recommend.get('tracks')

    def sad_recommender(self):
       
        recommend = sp.recommendations(
            seed_genres = Recommender.random_selector(Sad),
            limit = 10,
            country = 'IN',
            max_energy = 0.5,
            max_valence = 0.5,
            min_popularity = 30
        )
        tracks = recommend.get('tracks')
        for i in range(10):
            song_name = tracks[i]['name']
            song_id = tracks[i]['id']
            Recommender.song_name_list.append(song_name)
            Recommender.song_id_list.append(song_id)

        return Recommender.song_name_list, Recommender.song_id_list

    def anger_recommender(self):
           
        recommend = sp.recommendations(
            seed_genres = Recommender.random_selector(Anger),
            limit = 10,
            country = 'IN',
            min_energy = 0.5,
            max_valence = 0.5,
            min_popularity = 30
        )
        return recommend.get('tracks')
        
    def relaxed_recommender(self):
        song_name_list = []
        song_id_list = []
        recommend = sp.recommendations(
            seed_genres = Recommender.random_selector(Relaxed),
            limit = 10,
            country = 'IN',
            max_energy = 0.5,
            min_valence = 0.5,
            min_popularity = 30
        )
        tracks = recommend.get('tracks')
        return recommend.get('tracks')
        
rec = Recommender()
happy_song_name_info = rec.get_song_name_list(rec.happy_recommender())
# happy = recommendation.happy_recommender()
# sad = recommendation.sad_recommender()
# anger = recommendation.anger_recommender()
# relaxed = recommendation.relaxed_recommender()
print(token)
print(happy_song_name_info)


