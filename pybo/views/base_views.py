from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count

from ..models import Question


def index(request):
    return render(request, 'pybo/index.html')


def board(request):
    # 질문 목록 함수

    # 127.0.0.1:8000/pybo/board/?page=1 과 같은 의미다.
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    so = request.GET.get('so', 'recent')

    # 조회 --> DB에 있는 퀘스쳔모델을 가져옴   -를 붙이면 내림차순 정렬이 된다.
    #question_list = Question.objects.order_by('-create_date')

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:  # recent
        question_list = Question.objects.order_by('-create_date')

    # 검색
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색
        ).distinct()

    # 페이징처리               #페이지당 15개씩 보여주기
    paginator = Paginator(question_list, 15)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}  # {key : value}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    # 내용 출력 함수
    #question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


def profile(request):
    return render(request, 'pybo/profile.html')


def profile2(request):
    return render(request, 'pybo/profile2.html')

