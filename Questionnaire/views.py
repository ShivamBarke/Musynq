from django.shortcuts import render
from .models import Questionnaire ,XWeightage, YWeightage
from .serializers import QuestionnaireSerializer, XWeightageSerializer , YWeightageSerializer
from rest_framework import viewsets

# Create your views here.

class QuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all().order_by('userid')
    serializer_class = QuestionnaireSerializer

class XWeightageViewSet(viewsets.ModelViewSet):
    queryset = XWeightage.objects.all().order_by('QuestionNumber')
    serializer_class = XWeightageSerializer

class YWeightageViewSet(viewsets.ModelViewSet):
    queryset = YWeightage.objects.all().order_by('QuestionNumber')
    serializer_class = YWeightageSerializer

