
from django.urls import path
from .views import base_views, question_views, answer_views, comment_views, vote_views, test_views


# url 별칭 정하기 -> 네임 스페이스
app_name = 'pybo'

urlpatterns = [
    # base_views.py 로 연결
    path('', base_views.index, name='index'),
    path('board/', base_views.board, name='board'),
    path('<int:question_id>/', base_views.detail, name='detail'),
    path('profile/', base_views.profile, name='profile'),

    # question_views.py 로 연결
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete, name="question_delete"),

    # answer_views.py 로 연결
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),

    # comment_views.py 로 연결
    # question-comment
    path('comment/create/question/<int:question_id>/', comment_views.comment_create_question,
         name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', comment_views.comment_modify_question,
         name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', comment_views.comment_delete_question,
         name='comment_delete_question'),

    # answer-comment
    path('comment/create/answer/<int:answer_id>/', comment_views.comment_create_answer,
         name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_modify_answer,
         name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete_answer,
         name='comment_delete_answer'),


    # vote_views.py 로 연결
    path('vote/question/<int:question_id>/', vote_views.vote_question, name='vote_question'),
    path('vote/answer/<int:answer_id>/', vote_views.vote_answer, name='vote_answer'),


    # jq테스트용 test_views.py랑 연결
    path('test/jqtest/', test_views.jqtest, name='jqtest'),
    path('test/imgtest/', test_views.imgtest, name='imgtest'),
    path('test/market/', test_views.market, name='market'),
    path('test/components/', test_views.components, name='components'),
]
