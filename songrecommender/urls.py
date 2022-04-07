#this python files contains the the urls for the songrecommender app
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'MusynqUser', views.MusynqUserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework'))
]