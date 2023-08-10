from django.shortcuts import render
from pybo.models import Question, Answer
from rest_framework import viewsets
from django.contrib.auth.models import User


from . import serializers

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = serializers.AnswerSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.AnswerSerializer

def main(request):
    return render(request, 'main.html')