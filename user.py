import os
import spotipy
import spotipy.util as util
import playlists

os.environ["SPOTIPY_CLIENT_ID"] = "d04be567989d427e8ca8b0b27faa9bdc"
os.environ["SPOTIPY_CLIENT_SECRET"]= "07721eeec6e1493f80a52f79335f1a12"
os.environ["SPOTIPY_REDIRECT_URI"] = "https://www.google.com/"

username = '31vshd7issvkv2anywjv6q3ukxci'

try : 
    token = util.prompt_for_user_token(username)
except :
    os.remove(f'.cache-{username}')
    token = util.prompt_for_user_token(username)

sp = spotipy.Spotify(auth= token)

# sp.user_playlist_create()

