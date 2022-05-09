from .models import Questionnaire ,XWeightage, YWeightage
from .serializers import QuestionnaireSerializer, XWeightageSerializer , YWeightageSerializer, PostAnswerSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from requests import Request, post
from rest_framework.response import Response

# Create your views here.

class QuestionnaireView(generics.ListAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

    # def post(self, request, format=None):
    #     response = post()
    #     return 

class PostAnswerView(APIView):
    serializer_class = PostAnswerSerializer

    def post(self, request, format=None):
        if not request.session.exists(request.session.session_key):
            request.session.create()

        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            question1 = serializer.data.get('question1')
            question2 = serializer.data.get('question2')
            question3 = serializer.data.get('question3')
            question4 = serializer.data.get('question4')
            question5 = serializer.data.get('question5')
            question6 = serializer.data.get('question6')
            question7 = serializer.data.get('question7')
            question8 = serializer.data.get('question8')
            question9 = serializer.data.get('question9')
            question10 = serializer.data.get('question10')
            userid = request.session.session_key

            queryset = Questionnaire.objects.filter(userid= userid)

            if queryset.exists():
                answer = queryset[0]
                answer.question1 = question1
                answer.question2 = question2
                answer.question3 = question3
                answer.question4 = question4
                answer.question5 = question5
                answer.question6 = question6
                answer.question7 = question7
                answer.question8 = question8
                answer.question9 = question9
                answer.question10 = question10
                answer.save(update_fields = ['question1', 'question2','question3', 'question4', 'question5', 'question6','question7','question8','question9', 'question10'])
                return Response(PostAnswerSerializer(answer).data, status = status.HTTP_200_OK)
            else: 
                answer = Questionnaire(userid=userid,question1=question1,question2=question2,question3=question3,question4=question4,question5=question5,question6=question6,question7=question7,question8=question8,question9=question9,question10=question10)
                answer.save()
                return Response(PostAnswerSerializer(answer).data, status = status.HTTP_201_CREATED)

        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)




class XWeightageView(APIView):
    queryset = XWeightage.objects.all()
    serializer_class = XWeightageSerializer

class YWeightageView(APIView):
    queryset = YWeightage.objects.all()
    serializer_class = YWeightageSerializer

