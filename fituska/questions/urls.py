from django.urls import include, path
from . import views

urlpatterns = [
    path('questions/',views.temple_questions,name='questions'),
]