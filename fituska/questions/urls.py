from django.urls import path

from . import views


urlpatterns = [
    path('<str:shortcut>/<int:year>/', views.list_questions, name='questions'),
    path('<str:shortcut>/<int:year>/add/', views.add_question, name='add_question'),
    path('<str:shortcut>/<int:year>/<int:question_id>/', views.detail_question, name='question'),
    path('<str:shortcut>/<int:year>/<int:question_id>/add/', views.add_answer, name='add_answer'),
    path('<str:shortcut>/<int:year>/<int:question_id>/close/', views.close_question, name='close_question'),
    path('<str:shortcut>/<int:year>/<int:question_id>/<int:answer>/add/', views.add_reaction, name='add_reaction'),
    #path('<str:shortcut>/<int:year>/<int:question_id>/<int:answer_id>/close/', views.close_answer, name='close_answer'),
    path('<str:shortcut>/<int:year>/<int:question_id>/<int:answer_id>/rate/', views.rate_answer, name='rate'),
]
