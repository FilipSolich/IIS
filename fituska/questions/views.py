from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST

from .forms import AnswerForm, QuestionForm, ConfirmAnswerForm, FilterCategoryForm
from .models import Answer, Question, Rating
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


def add_question(request, shortcut, year):
    subject = get_object_or_404(Subject, shortcut=shortcut, year=year)
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.subject = subject
            question.save()

            return redirect('questions', shortcut, year)
    else:
        form = QuestionForm(subject=subject)

    return render(request, 'questions/add_question.html', {'form': form, 'subject': subject})


def detail_question(request, shortcut, year, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = Answer.objects.filter(question=question)
    answers_forms = [
        (answer, ConfirmAnswerForm(inittial={'answer_id': answer.id})) for answer in answers
    ]

    return render(request, 'questions/question.html', {
        'questions': question,
        'answers_forms': answer_forms
    })


def add_answer(request, shortcut, year, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST, request.FILES)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()

            return redirect('question', shortcut, year, question_id)
    else:
        form = AnswerForm()

    return render(request, 'questions/add_answer.html', {'form': form, 'question': question})


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


@require_POST
@login_required
def rate_answer(request, shortcut, year, question_id, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    type_ = request.POST.get('type')
    rate = Rating.objects.get(user=request.user, answer=answer)
    if not rate:
        rate = Rating.objects.create(type=type_, user=request.user, answer=answer)
        rate.save()
        answer.add_points(type_)
    else:
        if rate.type != type_:
            rate.type = type_
            rate.save()
            answer.add_points(type_, value=2)

    return HttpResponse()
