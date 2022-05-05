from django.shortcuts import render , redirect
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
# from ..Questionnaire.playlists import Playlists
# from ..Questionnaire import accesstoken
import spotipy.oauth2 as oauth
from requests import Request, post
from .credentials import REDIRECT_URI, CLIENT_SECRET, CLIENT_ID
from .util import *
from Questionnaire.models import Questionnaire

# token = accesstoken.get_token()
# pl = Playlists()

class AuthURL(APIView):
    def get(self, request, fornat=None):
        scopes = 'playlist-modify-public playlist-modify-private playlist-read-collaborative playlist-read-private user-read-email user-read-currently-playing user-modify-playback-state user-read-playback-state'
    

        url = Request('GET', 'https://accounts.spotify.com/authorize', params={
            'scope': scopes,
            'response_type': 'code',
            'redirect_uri': REDIRECT_URI,
            'client_id': CLIENT_ID
        }).prepare().url

        return Response({'url': url}, status=status.HTTP_200_OK)

def spotify_callback(request, format=None):
    code = request.GET.get('code')
    error = request.GET.get('error')

    response = post('https://accounts.spotify.com/api/token', data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }).json()

    access_token = response.get('access_token')
    token_type = response.get('token_type')
    refresh_token = response.get('refresh_token')
    expires_in = response.get('expires_in')
    error = response.get('error')

    if not request.session.exists(request.session.session_key):
        request.session.create()

    update_or_create_user_tokens(
        request.session.session_key, access_token, token_type, expires_in, refresh_token)

    return redirect('frontend:')

class IsAuthenticated(APIView):
    def get(self, request, format=None):
        is_authenticated = is_spotify_authenticated(
            self.request.session.session_key)
        return Response({'status': is_authenticated}, status=status.HTTP_200_OK)
    
class RecommendSongs(APIView):
    def get(self, request, format=None):
        userid = self.request.session.session_key
        user = SpotifyToken.objects.filter(user=userid)
        if user.exists():
            user = user[0]
        else: 
            return Response({}, status = status.HTTP_404_NOT_FOUND)
        
        spotify_id = get_spotify_id(userid)
        
        response = {
            'spotify_id': spotify_id,

        }

        return Response(response, status = status.HTTP_200_OK)

# class MusynqUserView(APIView):
#     queryset = MusynqUser.objects.all()
#     serializer_class = MusynqUserSerializer

# class LoginView(APIView):
#     serializer_class = MusynqUserSerializer
    
#     def post(self, request, format=None):
#         if not self.request.session.exists(self.request.session.session_key):
#             self.request.session.create()

#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             name =  self.request.session.session_key
#             queryset = MusynqUser.objects.filter(name=name)
#             spotifyid = pl.get_user_id(token= token)
#             if queryset.exists():
#                 user = queryset[0]
#                 user.save(update_fields = ['name', 'spotifyid'])
#                 return Response(MusynqUserSerializer(user).data, status = status.HTTP_200_OK)
#             else : 
#                 user = MusynqUserSerializer(name = name, spotifyid=spotifyid)
#                 user.save()
#                 return Response(MusynqUserSerializer(user).data, status = status.HTTP_201_CREATED)

#         return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)