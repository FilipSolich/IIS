from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404

from subjects.models import Subject


def teacher_required(view):
    return _role_on_subject(view, 'is_teacher')


def student_required(view):
    return _role_on_subject(view, 'is_student')


def _role_on_subject(view, method):
    def inner(request, *args, **kwargs):
        subject = get_object_or_404(Subject, shortcut=kwargs['shortcut'], year=kwargs['year'])
        if not request.user.is_anonymous and getattr(request.user, method)(subject):
            return view(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    return inner
