from django.db import models

# 질문 모델(테이블)
class Question(models.Model):
    subject = models.CharField(max_length=200) #제목 200자. 한글로 하면 100자
    content = models.TextField()               # 내용
    create_date = models.DateTimeField()       # 날자

    def __str__(self):
        return self.subject


# 답변 모델(테이블)
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # 외래키의 제약조건을 무시하고 연쇄 삭제됨. 즉 질문을 삭제하면 답변도 삭제됨.
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return str(self.question)
