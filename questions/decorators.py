from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404

from .models import Answer, Question


def question_not_closed(view):
    def inner(request, *args, **kwargs):
        question = get_object_or_404(Question, pk=kwargs['question_id'])
        if not question.closed:
            return view(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    return inner
