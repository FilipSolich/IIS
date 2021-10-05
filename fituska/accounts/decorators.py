from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404


def teacher_required(view):
    def inner(request, *args, **kwargs):
        subject = get_object_or_404(Subject, pk=kwargs.get('subject_id'))
        if subject.teacher != request.user:
            return HttpResponseForbidden()
        else:
            return view(request, *args, **kwargs)
    return inner
