from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MusynqUserSerializer
from .models import MusynqUser

# def landing_page(request):
#     return render(request,'index.html')

class MusynqUserViewSet(viewsets.ModelViewSet):
    queryset = MusynqUser.objects.all().order_by('name')
    serializer_class = MusynqUserSerializer
