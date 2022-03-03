import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

username = ''
token = util.prompt_for_user_token(username)

try : 
    token = util.prompt_for_user_token(username)
except :
    os.remove(f'.cache-{username}')
    token = util.prompt_for_user_token(username)

sp = spotipy.Spotify(auth= token)
auth_manager = spotipy.SpotifyClientCredentials()

print(token)