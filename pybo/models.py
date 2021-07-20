from django.db import models
from django.contrib.auth.models import User


# 질문 모델(테이블)
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200) #제목 200자. 한글로 하면 100자
    content = models.TextField()               # 내용
    create_date = models.DateTimeField()       # 날자 시간
    modify_date = models.DateTimeField(null=True, blank=True) # 수정한시간
                                 #값이 없어도 됨, 유효성검사를 안거쳐도 됨.

    def __str__(self):
        return self.subject


# 답변 모델(테이블)
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 외래키의 제약조건을 무시하고 연쇄 삭제됨. 즉 질문을 삭제하면 답변도 삭제됨.
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content


# 댓글 모델
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)


