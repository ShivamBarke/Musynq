from django.shortcuts import render
from .models import Questionnaire
from .serializers import QuestionnaireSerializer
from rest_framework import viewsets

# Create your views here.

class QuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all().order_by('userid')
    serializer_class = QuestionnaireSerializer 