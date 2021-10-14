from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.decorators.http import require_POST

from .forms import FilterLeaderboardForm, UserCreationForm
from .models import User, Karma
from subjects.models import Subject
from utils import get_unique_values



class LoginView(auth_views.LoginView):

    template_name = 'accounts/login.html'


class SignUpView(FormView):

    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('list_subjects')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


def leaderboard(request):
    subjects = Subject.objects.all()
    years = get_unique_values(subjects, '-year')
    shortcuts = get_unique_values(subjects, 'shortcut')

    form = FilterLeaderboardForm(request.GET, shortcuts=shortcuts, years=years)
    context = {'form': form}

    shortcut = request.GET.get('shortcut')
    year = request.GET.get('year')

    if shortcut == '--' or year == '--':
        shortcut = None
        year = None

    try:
        subject = Subject.objects.get(shortcut=shortcut, year=year)
    except Subject.DoesNotExist:
        users = sorted(User.objects.all(), key=lambda user: user.karma, reverse=True)
        context.update({'users': users})
    else:
        sub_karma = Karma.objects.filter(subject=subject).order_by('-karma')
        context.update({'sub_karma': sub_karma})

    return render(request, 'accounts/leaderboard.html', context)


@user_passes_test(lambda u: u.is_superuser)
def list_users(request):
    users = User.objects.all()
    mods = users.filter(is_moderator=True)
    return render(request, 'accounts/list_users.html', {'users': users, 'mods': mods})


@require_POST
@user_passes_test(lambda u: u.is_superuser)
def delete_user(request):
    get_object_or_404(User, pk=request.POST.get('user_id')).delete()
    return redirect('list_users')


@require_POST
@user_passes_test(lambda u: u.is_superuser)
def make_moderator(request):
    user = get_object_or_404(User, pk=request.POST.get('user_id'))
    group = Group.objects.get(name='Moderators')
    if not group in user.groups.all():
        user.groups.add(group)
        user.save()

    return redirect('list_users')


@require_POST
@user_passes_test(lambda u: u.is_superuser)
def delete_moderator(request):
    user = get_object_or_404(User, pk=request.POST.get('user_id'))
    group = Group.objects.get(name='Moderators')
    user.groups.remove(group)
    user.save()
    return redirect('list_users')
