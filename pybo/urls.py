
from django.urls import path
from pybo import views

# url 별칭 정하기 -> 네임 스페이스
app_name = 'pybo'

urlpatterns = [
    # base_views.py 로 연결
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),

    # question_views.py 로 연결
    path('question/create/', views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name="question_delete"),

    # answer_views.py 로 연결
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),

    # comment_views.py 로 연결
    # question-comment
    path('comment/create/question/<int:question_id>/', views.comment_create_question,
         name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', views.comment_modify_question,
         name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', views.comment_delete_question,
         name='comment_delete_question'),

    # answer-comment
    path('comment/create/answer/<int:answer_id>/', views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', views.comment_delete_answer, name='comment_delete_answer'),



    # jq테스트용
    path('test/jqtest/', views.jqtest, name='jqtest'),
    path('test/imgtest/', views.imgtest, name='imgtest'),
    path('test/market/', views.market, name='market'),
    path('test/components/', views.components, name='components'),
]
