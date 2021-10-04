from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.views.decorators.http import require_POST


def list_subjects(request):
    return render(request, 'subjects/subjects.html')


@login_required
def create_subject(request):
    pass


@user_passes_test(lambda x: x.is_moderator or x.is_superuser)
def confirm_subject(request):
    pass


# TODO teacher
def create_category(request, subject_id):
    pass


# TODO teacher
@require_POST
def delete_category(request, subject_id):
    pass


# TODO teacher
def students(request, subject_id):
    pass


@require_POST
@login_required
def register_subject(request, subject_id):
    pass
