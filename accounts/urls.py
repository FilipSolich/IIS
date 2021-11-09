from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.auth_views.logout_then_login, name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),

    path('leaderboard/', views.leaderboard, name='leaderboard'),

    path('admin/users/', views.list_users, name='list_users'),
    path('admin/users/delete/', views.delete_user, name='delete_user'),
    path('admin/moderators/', views.make_moderator, name='make_moderator'),
    path('admin/moderators/delete/', views.delete_moderator, name='delete_moderator'),
]
