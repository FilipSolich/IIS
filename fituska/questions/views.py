import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .decorators import answer_not_closed, question_not_closed
from .forms import AnswerForm, QuestionForm, QuestionCloseForm, FilterCategoryForm, ReactionForm
from .models import Answer, Question, Rating, Reaction
from accounts.decorators import teacher_required, student_required
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


# TODO: remove form for teacher points
# TODO: handle closed question
def detail_question(request, shortcut, year, question_id,
                    old_answer_form=None, old_reaction_form=None, old_close_form=None):
    subject = get_object_or_404(Subject, shortcut=shortcut, year=year)
    question = get_object_or_404(Question, pk=question_id)
    answers = Answer.objects.filter(question=question)

    answers_and_reactons = []
    for answer in answers:
        reactions = Reaction.objects.filter(answer=answer)

        if old_reaction_form and answer.id == old_reaction_form.answer_id:
            reaction_form = old_reaction_form
        elif (request.user.is_anonymous or
                not request.user.is_student(subject) and not request.user.is_teacher(subject)):
            reaction_form = None
        else:
            reaction_form = ReactionForm(initial={'answer_id': answer.id})

        try:
            rate = Rating.objects.get(user=request.user, answer=answer)
        except (Rating.DoesNotExist, TypeError):
            rate = None

        answers_and_reactons.append((answer, reactions, reaction_form, rate,))

    try:
        user_answer = Answer.objects.get(question=question, user=request.user)
    except (Answer.DoesNotExist, TypeError):
        user_answer = False

    if old_answer_form:
        answer_form = old_answer_form
    elif (request.user.is_anonymous or user_answer or request.user.is_teacher(subject) or
            not request.user.is_student(subject)):
        answer_form = None
    else:
        answer_form = AnswerForm()

    if old_close_form:
        close_form = old_close_form
    elif request.user.is_anonymous or request.user.is_student(subject):
        close_form = None
    else:
        close_form = QuestionCloseForm()

    return render(request, 'questions/question.html', {
        'subject': subject,
        'question': question,
        'is_teacher': not  request.user.is_anonymous and request.user.is_teacher(subject),
        'answers_and_reactions': answers_and_reactons,
        'answer_form': answer_form,
        'close_form': close_form,
    })


@question_not_closed
@student_required
@require_POST
def add_answer(request, shortcut, year, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        Answer.objects.get(question=question, user=request.user)
        return HttpResponseBadRequest()
    except Answer.DoesNotExist:
        pass

    form = AnswerForm(request.POST, request.FILES)
    if form.is_valid():
        answer = form.save(commit=False)
        answer.user = request.user
        answer.question = question
        answer.save()

        # Add 1 upvote from answer author
        Rating.objects.create(type=True, user=request.user, answer=answer)

        return redirect('question', shortcut, year, question_id)

    return redirect('question', shortcut, year, question_id, old_answer_form=form)


@teacher_required
@require_POST
def close_question(request, shortcut, year, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.closed = True
    question.save()

    answers = Answer.objects.filter(question=question)
    for answer in answers:
        if answer.valid:
            karma, _ = Karma.objects.get_or_create(user=answer.user, subject=answer.subject)
            karma.karma += answer.sum_points()
            karma.save()

    # TODO: add form for teacher points
    return redirect('question', shortcut, year, question_id)


@answer_not_closed
@question_not_closed
@student_required
def add_reaction(request, shortcut, year, question_id, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)

    form = ReactionForm(request.POST)
    if form.is_valid():
        reaction = form.save(commit=False)
        reaction.user = reqeust.user
        reaction.answer = answer
        reaction.save()

        return redirect('question', shortcut, year, question_id)

    return redirect('question', shortcut, year,question_id, old_reaction_form=form)


#@csrf_exempt
#@teacher_required
#@require_POST
#def close_answer(request, shortcut, year, question_id, answer_id):
#    valid = True if 'valid' in request.POST.keys() else False
#    answer = get_object_or_404(Answer, pk=answer_id)
#    form = CloseAnswerForm(request.POST)
#    if form.is_valid():
#        answer.valid = valid
#        answer.teacher_points = form.cleaned_data.get('teacher_points', 0) if valid else 0
#        answer.save()
#
#        return redirect('question', shortcut, year, question_id)
#
#    return redirect('question', shortcut, year, question_id, old_close_answer_form=form)


@csrf_exempt
@answer_not_closed
@question_not_closed
@login_required
@require_POST
def rate_answer(request, shortcut, year, question_id, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    question = get_object_or_404(Question, pk=question_id)
    type_ = json.loads(request.body).get('type')

    user_ratings = Rating.objects.filter(user=request.user, answer__question=question).count()

    try:
        rate = Rating.objects.get(user=request.user, answer=answer)

        if rate.type != type_:
            rate.type = type_
            rate.save()
        else:
            rate.delete()
    except Rating.DoesNotExist:
        if user_ratings >= 3:
            return HttpResponseBadRequest()

        Rating.objects.create(type=type_, user=request.user, answer=answer)

    return JsonResponse({'id': answer_id, 'type': type_})
