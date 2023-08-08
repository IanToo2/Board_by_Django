from pybo.models import Question, Answer
from rest_framework import serializers

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['author', 'modify_date', 'subject', 'content','create_date']

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ['author', 'modify_date', 'question', 'content','create_date']