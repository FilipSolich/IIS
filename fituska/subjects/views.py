from django.contrib.auth.decorators import login_required, permission_required
from django.http import response, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from accounts.decorators import teacher_required
from .models import Subject
from .forms import AddSubjectForm


def list_subjects(request):
    ordered_subject_list = Subject.objects.all()
    return render(request, 'subjects/subjects.html', {'ordered_subject_list': ordered_subject_list})


@login_required
def create_subject(request):
    pass

@permission_required('subjects.can_confirm_subject')
def new_subjects(request):
    if request.method == 'POST':
        form = AddSubjectForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = AddSubjectForm()
    return render(request, 'subjects/new.html', {'form': form})


@permission_required('subjects.can_confirm_subject')
def confirm_subject(request):
    pass


@permission_required('subjects.can_confirm_subject')
def reject_subject(request):
    pass


def subject_questions(request, subject_id):

    try:
        subject = Subject.objects.get(pk = subject_id)
    except:
        raise response.Http404("Subject does not exist")
    return render(request, 'subjects/questions.html', {'subject': subject})


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
