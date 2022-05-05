#this python files contains the the urls for the songrecommender app
from django.urls import path, include
from .views import AuthURL, RecommendSongs, spotify_callback, IsAuthenticated

urlpatterns = [
    path('get-auth-url', AuthURL.as_view()),
    path('redirect', spotify_callback),
    path('is-authenticated', IsAuthenticated.as_view()),
    path('recommend-songs', RecommendSongs.as_view())
]