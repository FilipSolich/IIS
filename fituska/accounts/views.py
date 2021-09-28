from django.shortcuts import get_object_or_404
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import Group
from django.http.response import HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import UserCreationForm
from .models import User

class LoginView(auth_views.LoginView):

    template_name = 'accounts/login.html'


class SignUpView(FormView):

    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid()


def make_moderator(request, user_id):
    if not request.user.is_admin:
        return HttpResponseForbidden()

    user = get_object_or_404(User, pk=user_id)
    group = Group.objects.get(name='Moderators')
    if not group in user.groups.all():
        user.groups.add(group)
        user.save()

    return HttpResponse()
