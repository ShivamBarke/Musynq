from .models import SpotifyToken
from django.utils import timezone
from datetime import timedelta
from .credentials import CLIENT_ID, CLIENT_SECRET
from requests import post, put, get, session
import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

BASE_URL = "https://api.spotify.com/v1"

Happy = ['hip hop', 'classical',' edm' ,'blues', 'country', 'funk', 'disco','love songs',' latino',' dubstep', 'punk', 'punk-rock' , 
            'heavy metal' , 'rock', 'rock-n-roll' ,'party','synth-pop', 'salsa', 'samba' ,'guitar', 'happy','alt-rock','indie', 'indie-pop','trance']

Sad = ['classical', 'broadway', 'blues','chill','sad','club', 'comedy']

Relaxed= ['classical' , 'new age', 'love songs', 'jazz',' latino', ' chill',' work-out','road-trip', 'opera', 'sleep','acoustic','hip-hop', 'holidays','movies','trance','drum-and-bass','new-age','club', 'comedy']

Anger= ['reggae' ,'club', 'death -metal','drum-and-bass',' dub', 'dubstep', 'edm', 'electro', 'electronic', 'emo','heavy metal','alt-rock','drum-and-bass']
    
Mood = [Happy, Sad, Anger, Relaxed]




song_name_list = []
song_id_list = []

def get_user_tokens(session_id):
    user_tokens = SpotifyToken.objects.filter(user=session_id)
    print(user_tokens)
    if user_tokens.exists():
        return user_tokens[0]
    else:
        return None


def update_or_create_user_tokens(session_id, access_token, token_type, expires_in, refresh_token):
    tokens = get_user_tokens(session_id)
    expires_in = timezone.now() + timedelta(seconds=expires_in)

    if tokens:
        tokens.access_token = access_token
        tokens.refresh_token = refresh_token
        tokens.expires_in = expires_in
        tokens.token_type = token_type
        tokens.save(update_fields=['access_token',
                                   'refresh_token', 'expires_in', 'token_type'])
    else:
        tokens = SpotifyToken(user=session_id, access_token=access_token,
                              refresh_token=refresh_token, token_type=token_type, expires_in=expires_in)
        tokens.save()

def is_spotify_authenticated(session_id):
    tokens = get_user_tokens(session_id)
    if tokens:
        expiry = tokens.expires_in
        if expiry <= timezone.now():
            refresh_spotify_token(session_id)

        return True

    return False

def refresh_spotify_token(session_id):
    refresh_token = get_user_tokens(session_id).refresh_token

    response = post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()

    access_token = response.get('access_token')
    token_type = response.get('token_type')
    expires_in = response.get('expires_in')
    refresh_token = response.get('refresh_token')

    update_or_create_user_tokens(
        session_id, access_token, token_type, expires_in, refresh_token)


def execute_spotify_api_request(session_id, endpoint, post_=False, put_=False):
    tokens = get_user_tokens(session_id)
    headers = {'Content-Type': 'application/json',
               'Authorization': "Bearer " + tokens.access_token}
    data = {}
    if post_:
        post(BASE_URL + endpoint, headers=headers, data=data)
    elif put_:
        put(BASE_URL + endpoint, headers=headers)
    else : 
        response = get(BASE_URL + endpoint, {}, headers=headers)
    try:
        return response.json()
    except:
        return {'Error': 'Issue with request'}

def execute_spotify_post_request(session_id, endpoint):
    tokens = get_user_tokens(session_id)
    headers = {'Content-Type': 'application/json',
               'Authorization': "Bearer " + tokens.access_token}
    data = {}

    response = post(BASE_URL + endpoint, headers=headers, data=data)
    return response.json()

def random_selector(self , list: list) :
        for i in range(5):
            list1 = random.choices(list, k=5)
        return list1 

def get_spotify_id(session_id):
    endpoint = ""
    response = execute_spotify_api_request(session_id=session_id,endpoint=endpoint)
    spotify_id = response.get('id')
    return spotify_id

# def create_playlist(session_id, pl_name:str ):
#     user_id = get_spotify_id(session_id)
#     endpoint = f"/users/{user_id}/playlists"
#     tokens = get_user_tokens(session_id)
#     headers = {'Content-Type': 'application/json',
#                'Authorization': "Bearer " + tokens.access_token}
#     data = {"name": pl_name}
#     response = post(BASE_URL + endpoint, headers=headers, data=data)
#     playlist_id = response.get('external_urls')
#     return playlist_id

def get_recommendations(session_id,self, mood:list, energy:float, valence:float):
    tokens = get_user_tokens(session_id)
    sp = spotipy.Spotify(auth = tokens)
    recommend = sp.recommendations(
            seed_genres = mood,
            limit = 10,
            country = 'IN',
            target_energy = energy,
            target_valence = valence,
            min_popularity = 45
        )
    return recommend.get('tracks')

def get_song_id_list(self, tracks):
        for i in range(10):
            song_id = tracks[i]['id']
            song_id_list.append(song_id)
        return song_id_list

def add_songs(session_id,pl_name:str, mood:list, energy:float, valence:float):
    tokens = get_user_tokens(session_id)
    sp = spotipy.Spotify(auth = tokens)
    create = sp.user_playlist_create(get_spotify_id(), pl_name)    
    moods = random_selector(list= mood)
    mood_songs = get_recommendations(mood = moods, energy = energy, valence = valence)
    playlist_id = str(create['id'])
    songs_id = get_song_id_list(tracks = mood_songs)
    added_playlist = sp.playlist_add_items(playlist_id, songs_id)
    return added_playlist




# def add_songs(session_id):
#     user_id = get_spotify_id(session_id)
#     endpoint= "/playlists/playlist_id/tracks"
#     tokens = get_user_tokens(session_id)
#     headers = {'Content-Type': 'application/json',
#                'Authorization': "Bearer " + tokens.access_token}
#     data = {}
#     response = post(BASE_URL + endpoint, headers=headers, data=data)
#     return