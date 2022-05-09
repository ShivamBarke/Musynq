from django.urls import path, include

from Questionnaire.serializers import PostAnswerSerializer
from .views import PostAnswerView, QuestionnaireView, XWeightageView, YWeightageView

urlpatterns = [
    path('questions', QuestionnaireView.as_view()),
    path('xweightage', XWeightageView.as_view()),
    path('yweightage', YWeightageView.as_view()),
    path('post-answers', PostAnswerView.as_view())
    
]