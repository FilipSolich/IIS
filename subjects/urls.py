from django.urls import path

from . import views


urlpatterns = [
    path('', views.create_subject, name='create_subject'),
    path('new/', views.new_subjects, name='new_subjects'),
    path('new/confirm/<int:subject_id>', views.confirm_subject, name='confirm_subject'),
    path('new/reject/<int:subject_id>', views.reject_subject, name='reject_subject'),
    path('<int:subject_id>/', views.subject_questions, name='subject_questions'),
    path('<int:subject_id>/categories/', views.create_category, name='create_category'),
    path('<int:subject_id>/categories/delete/', views.delete_category, name='delete_category'),
    path('<int:subject_id>/students/', views.students, name='students'),
    path('<int:subject_id>/students/confirm/', views.confirm_student, name='confirm_student'),
    path('<int:subject_id>/students/reject/', views.reject_student, name='reject_student'),
    path('<int:subject_id>/register/', views.register_subject, name='register_subject'),
]
