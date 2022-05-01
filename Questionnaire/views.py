from .models import Questionnaire ,XWeightage, YWeightage
from .serializers import QuestionnaireSerializer, XWeightageSerializer , YWeightageSerializer
from rest_framework import generics, status
from rest_framework.views import APIView

# Create your views here.

class QuestionnaireView(generics.ListAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

class XWeightageView(APIView):
    queryset = XWeightage.objects.all()
    serializer_class = XWeightageSerializer

class YWeightageView(APIView):
    queryset = YWeightage.objects.all()
    serializer_class = YWeightageSerializer

