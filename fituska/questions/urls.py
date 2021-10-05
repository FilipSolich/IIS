from django.urls import path

from . import views


urlpatterns = [
    path('<str:shortcut>/<int:year>/', views.list_questions, name='questions'),
    path('<str:shortcut>/<int:year>/<int:question_id>/', views.detail_question, name='question'),
    path('<str:shortcut>/<int:year>/<int:question_id>/<int:answer_id>/confirm', views.confirm_answer, name='confirm_answer'),
    path('<str:shortcut>/<int:year>/<int:question_id>/<int:answer_id>/reject', views.reject_answer, name='reject_answer'),
    path('<str:shortcut>/<int:year>/<int:question_id>/<int:answer_id>/rate', views.rate_answer, name='rate'),
]
