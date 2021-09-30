from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.auth_views.logout_then_login, name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('make_moderator/<int:user_id>/', views.make_moderator, name='make_moderator'),
]
