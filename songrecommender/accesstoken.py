import os
import spotipy.util as util
import spotipy.oauth2 as oauth

os.environ["SPOTIPY_CLIENT_ID"] = "d04be567989d427e8ca8b0b27faa9bdc"
os.environ["SPOTIPY_CLIENT_SECRET"]= "07721eeec6e1493f80a52f79335f1a12"
os.environ["SPOTIPY_REDIRECT_URI"] = "http://127.0.0.1:8000/index.html"

OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'
OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'

scopes = ['playlist-modify-public',
    'playlist-modify-private',
    'playlist-read-collaborative',
    'playlist-read-private', 
    'user-read-email' , 
    'user-read-currently-playing',
    'user-modify-playback-state',
    'user-read-playback-state',
    ]

authorize = oauth.SpotifyOAuth(scope=scopes)

def get_token():
    token = authorize.get_access_token()
    # username = ''
    # token = util.prompt_for_user_token(username)

    # try : 
    #     token = util.prompt_for_user_token(username)
    # except :
    #     os.remove(f'.cache-{username}')
    #     token = util.prompt_for_user_token(username)

    return token['access_token']
