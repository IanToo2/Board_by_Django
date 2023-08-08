from pybo.models import Question, Answer
from rest_framework import viewsets
from . import serializers

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
