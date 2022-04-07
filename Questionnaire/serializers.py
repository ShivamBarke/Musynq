from rest_framework import serializers
from .models import Questionnaire

class QuestionnaireSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ('userid','question1', 'question2','question3', 'question4', 'question5', 'question6','question7','question8','question9', 'question10')
