from django.urls import path

from . import views


urlpatterns = [
    path('', views.create_subject, name='create_subject'),
    path('confirm/', views.confirm_subject, name='confirm_subject'),
    path('<int:subject_id>/categories/', views.create_category, name='create_category'),
    path('<int:subject_id>/categories/delete/', views.delete_category, name='delete_category'),
    path('<int:subject_id>/students/', views.students, name='students'),
    path('<int:subject_id>/register/', views.register_subject, name='register_subject'),
]

