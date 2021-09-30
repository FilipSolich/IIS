from django.urls import path

from . import views


urlpatterns = [
    path('<str:subject_name>/', views.questions_list, name='questions'),
    path('<str:subject_name>/<int:question_id>/', views.question_detail, name='question'),
    path('<str:subject_name>/<int:question_id>/<int:answer_id>/rate', views.answer_rate, name='rate'),
]
