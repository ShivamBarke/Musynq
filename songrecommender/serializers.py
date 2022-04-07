from random import choices
from re import I
from rest_framework import serializers
from .models import MusynqUser

class MusynqUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = MusynqUser
        fields = ('name', 'age', 'gender') 
    
