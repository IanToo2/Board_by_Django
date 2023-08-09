from django.db import models
from django.contrib.auth.models import User

# 모델에 함수가 추가될 경우 makemigrations와 migrate X
# 모델의 속성이 변경되었을 경우 사용

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    modify_date = models.DateTimeField(null=True, blank=True) # 수정일
    subject = models.CharField(max_length=200)
    content = models.TextField(default="No content available")
    create_date = models.DateTimeField(null=True)
    voter = models.ManyToManyField(User, related_name='voter_question') # 추천인

    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = True,  related_name='author_answer')
    modify_date = models.DateTimeField(null=True, blank=True) # 수정일
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField(default="No content available")
    create_date = models.DateTimeField(null=True)
    voter = models.ManyToManyField(User, related_name='voter_answer') # 추천인