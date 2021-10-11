from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from accounts.decorators import teacher_required
from .models import Subject
from .forms import AddSubjectForm

def list_subjects(request):
    return render(request, 'subjects/subjects.html', {})

#@user_passes_test(lambda x: x.is_moderator or x.is_superuser)    
def new_subjects(request):
    if request.method == 'POST':
        form = AddSubjectForm(request.POST)
        #if form.is_valid():
        form.save()
        return redirect("/")
    else:
        form = AddSubjectForm()
    return render(request, 'subjects/new.html', {'form': form})


@login_required
def create_subject(request):
    pass

@user_passes_test(lambda x: x.is_moderator or x.is_superuser)
def confirm_subject(request):
    pass


@user_passes_test(lambda x: x.is_moderator or x.is_superuser)
def reject_subject(request):
    pass


@teacher_required
def create_category(request, subject_id):
    pass

@require_POST
@teacher_required
def delete_category(request, subject_id):
    pass


@teacher_required
def students(request, subject_id):
    pass


@require_POST
@teacher_required
def confirm_student(request, subject_id):
    pass


@require_POST
@teacher_required
def reject_student(request, subject_id):
    pass


@require_POST
@login_required
def register_subject(request, subject_id):
    pass
