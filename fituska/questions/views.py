import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import AnswerForm, QuestionForm, ConfirmAnswerForm, FilterCategoryForm, ReactionForm
from .models import Answer, Question, Rating, Reaction
from accounts.decorators import teacher_required
from subjects.models import Category, Subject


def list_questions(request, shortcut, year):
    subject = get_object_or_404(Subject, shortcut=shortcut, year=year)
    category_form = FilterCategoryForm(request.GET, subject=subject)

    category_id = request.GET.get('category')

    if category_id == '--':
        category_id = None

    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        questions = Question.objects.filter(subject=subject)
    else:
        questions = Question.objects.filter(subject=subject, category=category)

    return render(request, 'questions/questions.html', {
        'subject': subject,
        'questions': questions,
        'category_form': category_form
    })


@login_required
def add_question(request, shortcut, year):
    subject = get_object_or_404(Subject, shortcut=shortcut, year=year)
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES, subject=subject)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.subject = subject
            question.save()

            return redirect('questions', shortcut, year)
    else:
        form = QuestionForm(subject=subject)

    return render(request, 'questions/add_question.html', {'form': form, 'subject': subject})


def detail_question(request, shortcut, year, question_id, form=None):
    subject = get_object_or_404(Subject, shortcut=shortcut, year=year)
    question = get_object_or_404(Question, pk=question_id)
    answers = Answer.objects.filter(question=question)

    answers_and_reactons = []
    for answer in answers:
        try:
            rate = Rating.objects.get(user=request.user, answer=answer)
        except (Rating.DoesNotExist, TypeError):
            rate = None

        reactions = Reaction.objects.filter(answer=answer)

        answers_and_reactons.append((
            answer, reactions, rate, ConfirmAnswerForm(initial={'answer_id': answer.id})
        ))

    try:
        user_answer = Answer.objects.get(question=question, user=request.user)
    except (Answer.DoesNotExist, TypeError):
        user_answer = False

    if form:
        answer_form = form
    elif request.user.is_anonymous or user_answer:
        answer_form = None
    else:
        answer_form = AnswerForm()

    return render(request, 'questions/question.html', {
        'subject': subject,
        'question': question,
        'answers_and_reactions': answers_and_reactons,
        'answer_form': answer_form,
    })


@require_POST
@login_required
def add_answer(request, shortcut, year, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        Answer.objects.get(question=question, user=request.user)
    except Answer.DoesNotExist:
        pass
    else:
        return HttpResponseBadRequest()

    form = AnswerForm(request.POST, request.FILES)
    if form.is_valid():
        answer = form.save(commit=False)
        answer.user = request.user
        answer.question = question
        answer.save()

        # Add 1 upvote from answer author
        rate = Rating.objects.create(type=True, user=request.user, answer=answer)
        rate.save()

        return redirect('question', shortcut, year, question_id)

    return redirect('question', shortcut, year, question_id, form=form)


@login_required
def add_reaction(request, shortcut, year, question_id, answer_id):
    pass


@require_POST
@teacher_required
def confirm_answer(request, shortcut, year, question_id, answer_id):
    form = ConfirmAnswerForm(request.POST)
    if form.is_valid():
        pass


@require_POST
@teacher_required
def reject_answer(request, shortcut, year, question_id, answer_id):
    pass


@csrf_exempt
@require_POST
@login_required
def rate_answer(request, shortcut, year, question_id, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    question = get_object_or_404(Question, pk=question_id)
    type_ = json.loads(request.body).get('type')

    user_ratings = Rating.objects.filter(user=request.user, answer__question=question).count()

    try:
        rate = Rating.objects.get(user=request.user, answer=answer)
    except Rating.DoesNotExist:
        rate = None
        
        if user_ratings >= 3:
            return HttpResponseBadRequest()

    if not rate:
        rate = Rating.objects.create(type=type_, user=request.user, answer=answer)
        rate.save()
    else:
        if rate.type != type_:
            rate.type = type_
            rate.save()
        else:
            rate.delete()

    return JsonResponse({'id': answer_id, 'type': type_})
