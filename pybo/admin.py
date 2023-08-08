from django.contrib import admin
from . import models

class AnswerInline(admin.TabularInline):
    model = models.Answer
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('author', 'modify_date', 'subject', 'content', 'create_date')
    list_filter=['subject']
    fieldsets = [
        (None, {'fields': ['author']}),
        ('제목 내용 !!!', {'fields': ['subject']}),
    ]
    inlines = [AnswerInline]
    
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('author', 'modify_date', 'question', 'content', 'create_date')
    list_filter=['content']
    fieldsets = [
        (None, {'fields': ['author']}),
        ('답글 내용 !!!', {'fields': ['content']}),
    ]

admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Answer, AnswerAdmin)
