from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.http.response import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404,render
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST, require_http_methods
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


def leaderboard(request):
    subject_id = request.GET.get('subject')
    if not subject_id:
        users = User.objects.all().order_by('-karma')
        context = {'users': users}
    else:
        subject = get_object_or_404(Subjects, pk=subject_id)
        sub_karma = Karma.objects.filter(subject=subject).order_by('-karma')
        context = {'sub_karma': sub_karma}

    return render(request, 'accounts/leaderboard.html', context)


@user_passes_test(lambda u: u.is_superuser)
def list_users(request):
    users = User.objects.all()
    return render(request, 'accounts/list_users.html', {'users': users})


@require_POST
@user_passes_test(lambda u: u.is_superuser)
def make_moderator(request):
    user = get_object_or_404(User, pk=request.POST.get('user_id'))
    group = Group.objects.get(name='Moderators')
    if not group in user.groups.all():
        user.groups.add(group)
        user.save()

    return HttpResponse()


@require_http_methods(['DELETE'])
@user_passes_test(lambda u: u.is_superuser)
def delete_moderator(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    group = Group.objects.get(name='Moderators')
    user.groups.remove(group)
    user.save()
    return HttpResponse()


@require_http_methods(['DELETE'])
@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, user_id):
    get_object_or_404(User, pk=user_id).delete()
    return HttpResponse()
