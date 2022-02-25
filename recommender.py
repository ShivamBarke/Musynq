# this file recommends songs based on the mood. 


import spotipy
import os
import json
import random
from spotipy.oauth2 import SpotifyClientCredentials


os.environ["SPOTIPY_CLIENT_ID"] = "d04be567989d427e8ca8b0b27faa9bdc"
os.environ["SPOTIPY_CLIENT_SECRET"]= "07721eeec6e1493f80a52f79335f1a12"
os.environ["SPOTIPY_REDIRECT_URI"] = "https://www.google.com/"

auth_manager = spotipy.SpotifyClientCredentials()

sp = spotipy.Spotify(auth_manager = auth_manager)


Happy = ['hip hop', 'classical',' edm' ,'blues', 'country', 'funk', 'disco','love songs',' latino',' dubstep', 'punk', 'punk-rock' , 
 'heavy metal' , 'rock', 'rock-n-roll' ,'party','synth-pop', 'salsa', 'samba' ,'guitar', 'happy','alt-rock','indie', 'indie-pop','trance']

Sad = ['classical', 'broadway', 'blues','chill','sad','club', 'comedy']

Relaxed= ['classical' , 'new age', 'love songs', 'jazz',' latino', ' chill',' work-out','road-trip', 'opera', 'sleep','acoustic','hip-hop', 'holidays','movies','trance','drum-and-bass','new-age','club', 'comedy']

Anger= ['reggae' ,'club', 'death -metal','drum-and-bass',' dub', 'dubstep', 'edm', 'electro', 'electronic', 'emo','heavy metal','alt-rock','drum-and-bass']


class Recommender():
    # Selects random song genres from above defined lists i.e happy sad angry relax

    # Add duration specific songs duration > 1 min
    
    def random_selector(list) :
        for i in range(5):
            list1 = random.choices(list, k=5)
        return list1    
    # Recommends MOOD wise playlists using spotipy library 
    def happy_recommender():
        song_name_list = []
        song_id_list = []
        recommend = sp.recommendations(
            seed_genres = Recommender.random_selector(Happy),
            limit = 10,
            country = 'IN',
            min_energy = 0.5,
            min_valence = 0.5,
            min_popularity = 30
        )
        tracks = recommend.get('tracks')
        for i in range(10):
            song_name = tracks[i].get('name')
            song_id = tracks[i].get('id')
            song_name_list.append(song_name)
            song_id_list.append(song_id)

        return song_name_list, song_id_list

    def sad_recommender():
        song_name_list = []
        song_id_list = []
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
            song_name = tracks[i].get('name')
            song_id = tracks[i].get('id')
            song_name_list.append(song_name)
            song_id_list.append(song_id)

        return song_name_list, song_id_list

    def anger_recommender():
            song_name_list = []
            song_id_list = []
            recommend = sp.recommendations(
                seed_genres = Recommender.random_selector(Anger),
                limit = 10,
                country = 'IN',
                min_energy = 0.5,
                max_valence = 0.5,
                min_popularity = 30
            )
            tracks = recommend.get('tracks')
            for i in range(10):
                song_name = tracks[i].get('name')
                song_id = tracks[i].get('id')
                song_name_list.append(song_name)
                song_id_list.append(song_id)

            return song_name_list, song_id_list

    def relaxed_recommender():
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
            for i in range(10):
                song_name = tracks[i].get('name')
                song_id = tracks[i].get('id')
                song_name_list.append(song_name)
                song_id_list.append(song_id)

            return song_name_list, song_id_list

happy = Recommender.happy_recommender()
sad = Recommender.sad_recommender()
anger = Recommender.anger_recommender()
relaxed = Recommender.relaxed_recommender()


