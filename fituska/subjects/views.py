from django.contrib.auth.decorators import login_required, permission_required
from django.http import response, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import Subject
from .forms import AddSubjectForm, FilterYearForm
from accounts.decorators import teacher_required
from utils import get_unique_values, get_current_school_years


def list_subjects(request):
    ordered_subject_list = Subject.objects.all()
    years = get_unique_values(ordered_subject_list, '-year')

    form = FilterYearForm(request.GET, years=years)

    year = request.GET.get('year')
    if not year or year == '--':
        year = get_current_school_years()
    ordered_subject_list = ordered_subject_list.filter(year=year)

    return render(request, 'subjects/subjects.html', {
        'ordered_subject_list': ordered_subject_list,
        'ordered_grade_list': get_unique_values(ordered_subject_list,"grade"),
        'ordered_semester_list': get_unique_values(ordered_subject_list,"-semester"),
        'ordered_compulsory_list': get_unique_values(ordered_subject_list,"compulsory"),
        'form': form
    })


@login_required
def create_subject(request):
    if request.method == 'POST':
        form = AddSubjectForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    else:
        form = AddSubjectForm()
    return render(request, 'subjects/new.html', {'form': form})


@permission_required('subjects.can_confirm_subject')
def new_subjects(request):
    pass


@permission_required('subjects.can_confirm_subject')
def confirm_subject(request):
    pass


@permission_required('subjects.can_confirm_subject')
def reject_subject(request):
    pass


def subject_questions(request, subject_id):

    try:
        subject = Subject.objects.get(pk = subject_id)
    except:
        raise response.Http404("Subject does not exist")
    return render(request, 'subjects/questions.html', {'subject': subject})


@teacher_required
def create_category(request, subject_id):
    pass

@require_POST
@teacher_required
def delete_category(request, subject_id):
    pass


@teacher_required
def students(request, subject_id):
    pass


@require_POST
@teacher_required
def confirm_student(request, subject_id):
    pass


@require_POST
@teacher_required
def reject_student(request, subject_id):
    pass


@require_POST
@login_required
def register_subject(request, subject_id):
    pass
