from django.contrib import admin
from core.quiz.models import Answer, Quiz, Score

# Register your models here.
admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(Score)