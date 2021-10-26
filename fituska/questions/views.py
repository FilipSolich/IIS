from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
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


@login_required
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


def detail_question(request, shortcut, year, question_id, form=None):
    question = get_object_or_404(Question, pk=question_id)
    answers = Answer.objects.filter(question=question)

    answers_and_forms = [
        (answer, ConfirmAnswerForm(initial={'answer_id': answer.id})) for answer in answers
    ]

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
        'question': question,
        'answers': answers_and_forms,
        'answer_form': answer_form,
    })


@require_POST
@login_required
def add_answer(request, shortcut, year, question_id):
    
    question = get_object_or_404(Question, pk=question_id)
    if Answer.objects.get(question=question, user=request.user):
        return HttpResponseBadRequest()
    form = AnswerForm(request.POST, request.FILES)
    if form.is_valid():
        answer = form.save(commit=False)
        answer.user = request.user
        answer.question = question
        answer.save()
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
