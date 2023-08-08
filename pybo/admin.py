from django.contrib import admin
from .models import Question
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    search_fileds = ['subject']

admin.site.register(Question, QuestionAdmin)