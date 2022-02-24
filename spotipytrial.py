from numpy import append
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import os
 
os.environ["SPOTIPY_CLIENT_ID"] = "d04be567989d427e8ca8b0b27faa9bdc"
os.environ["SPOTIPY_CLIENT_SECRET"]= "07721eeec6e1493f80a52f79335f1a12"

data = pd.read_csv('data/data.csv')
valence_values = pd.read_csv('data/data.csv', usecols= 'valence')


print(valence_values)
#sp is our spotify client from which we will be accessing all our apis/functions
#auth_manager is our client credential flow manager which is used to pass client credentials whenever necessary
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)
song = sp.track('6f3ANRNQ8nCiPZ6VqXqq93', market='IN')
song_name = song['name']
song_album_name = song['album']['name']
song_analysis = sp.audio_features('6f3ANRNQ8nCiPZ6VqXqq93')
print(song_analysis)
# print(song_name, song_album_name)


# sp.recommendations()

