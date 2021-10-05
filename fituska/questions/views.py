from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST

from .models import Answer, Question, Rating
from accounts.decorators import teacher_required
from subjects.models import Subject


# TODO Dodelat vyhledavani
def list_questions(request, shortcut, year):
    subject = get_object_or_404(Subject, shortcut=shortcut, year=year)
    questions = Question.objects.filter(subject=subject)
    return render(request, 'questions/questions.html', {'questions': questions})


def detail_question(request, shortcut, year, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'questions/question.html', {'questions': question})


@teacher_required
@require_POST
def confirm_answer(request, shortcut, year, question_id, answer_id):
    pass


@teacher_required
@require_POST
def reject_answer(request, shortcut, year, question_id, answer_id):
    pass


def _add_points_to_answer(answer, type_, value=1):
    if type_:
        answer.points += value
    else:
        answer.points -= value

    answer.save()


@require_POST
@login_required
def rate_answer(request, shortcut, year, question_id, answer_id):
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
