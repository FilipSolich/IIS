from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Answer, Question, Rating
from subjects.models import Subject


# TODO Dodelat vyhledavani
def questions_list(request, subject_name):
    subject = get_object_or_404(Subject, name=subject_name)
    questions = Question.objects.filter(subject=subject)
    return render(request, 'questions/questions.html', {'questions': questions})


def question_detail(request, subject_name, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'questions/question.html', {'questions': question})


def _add_points_to_answer(answer, type_, value=1):
    if type_:
        answer.points += value
    else:
        answer.points -= value

    answer.save()


@login_required
def answer_rate(request, answer_id, **kwargs):
    answer = get_object_or_404(Answer, pk=answer_id)
    type_ = request.POST.get('type')
    rate = Rating.objects.get(user=request.user, answer=answer)
    if not rate:
        rate = Rating.objects.create(type=type_, user=request.user, answer=answer)
        rate.save()
        _add_points_to_answer(answer, type_)
    else:
        if rate.type != type_:
            rate.type = type_
            rate.save()
            _add_points_to_answer(answer, type_, value=2)

    return HttpResponse()
