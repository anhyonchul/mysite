from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question, Answer
from django.utils import timezone

def index(request):
    # DB에 있는 퀘스쳔모델을 가져옴            -를 붙이면 내림차순 정렬이 된다.
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list' : question_list}  # {key : value}
    return render(request, 'pybo/question_list.html' ,context)
    #return HttpResponse("Welcome!!! pybo에 오신것을 환영합니다.")

def detail(request, question_id):
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)

# 1. html 만들기 2. urls에 경로 추가하기 3. views.py에서 랜더링하기

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)
     #똑같은 페이지에 나올수 있게 하는 redirect