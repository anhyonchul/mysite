from django.contrib import admin

# 모델 등록

from .models import Question, Answer

admin.site.register(Question)
admin.site.register(Answer)