from django.urls import path, include
from .views import QuestionnaireView, XWeightageView, YWeightageView

urlpatterns = [
    path('questions', QuestionnaireView.as_view()),
    path('xweightage', XWeightageView.as_view()),
    path('yweightage', YWeightageView.as_view())
    
]