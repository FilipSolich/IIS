from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404

from subjects.models import Subject


def teacher_required(view):
    def inner(request, *args, **kwargs):
        subject = get_object_or_404(Subject, shortcut=kwargs.get('shortcut'), year=kwargs.get('year'))
        if request.user.is_teacher(subject):
            return view(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return inner
