from django.contrib.auth import views as auth_views
from django.urls import path

from .views import LoginView, SignUpView, make_moderator


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.logout_then_login, name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('make_moderator/<int:user_id>/', make_moderator, name='make_moderator'),
]
