from django.contrib.auth.decorators import login_required, permission_required
from django.http import response, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import Subject,Category
from .forms import AddSubjectForm, ConfirmSubjectForm, FilterYearForm, AddCategoryForm
from accounts.decorators import teacher_required
from utils import get_unique_values, get_current_school_year


def list_subjects(request):
    ordered_subject_list = Subject.objects.all()
    years = get_unique_values(ordered_subject_list, '-year')
    current_year = get_current_school_year()
    if not current_year in years:
        years.insert(0, current_year)

    form = FilterYearForm(request.GET, years=years, default_none=False)

    year = request.GET.get('year')
    if not year or year == '--':
        year = current_year
    ordered_subject_list = ordered_subject_list.filter(year=year)

    comp = []
    uncomp = []
    for subj in ordered_subject_list:
        if subj.compulsory == "compulsory":
            comp.append(subj)
        else:
            uncomp.append(subj)


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
            subject = form.save(commit = False)
            subject.user = request.user
            subject.save()
        return redirect("/")
    else:
        form = AddSubjectForm()
    return render(request, 'subjects/new.html', {'form': form})


@permission_required('subjects.can_confirm_subject')
def new_subjects(request):
    unconfirmed_subjects = Subject.objects.filter(confirmed=False)
    return render(request, 'subjects/unconfirmed.html', {'unconfirmed_subjects': unconfirmed_subjects})

@permission_required('subjects.can_confirm_subject')
def confirm_subject(request, subject_id):
    subject = Subject.objects.get(id = subject_id)
    if request.method == 'POST':
        
        form = ConfirmSubjectForm(request.POST, instance=subject)

        if form.is_valid():
            subject = form.save(commit=False)
            subject.save()
            return redirect("/subjects/new")

    else:
        form = ConfirmSubjectForm()
         
    return render(request, 'subjects/edit_subject.html', {'subject': subject, 'form': form})

@permission_required('subjects.can_confirm_subject')
def reject_subject(request, subject_id):
    subject = Subject.objects.get(id = subject_id)
    if request.method == 'POST':
        
        form = ConfirmSubjectForm(request.POST, instance=subject)

        if form.is_valid():
            subject.delete()
            return redirect("/subjects/new")

    else:
        form = ConfirmSubjectForm()
         
    return render(request, 'subjects/edit_subject.html', {'subject': subject, 'form': form})


def subject_questions(request, subject_id):

    try:
        subject = Subject.objects.get(pk = subject_id)
    except:
        raise response.Http404("Subject does not exist")
    return render(request, 'subjects/questions.html', {'subject': subject})


@teacher_required
def create_category(request, subject_id):

    category = Category.objects.filter(pk = subject_id)
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            cat = form.save(commit = False)
            cat.save()
            return redirect("/")
    else:
        form = AddCategoryForm()
    return render(request, 'subjects/new_category.html', {'category': category,'form': form})

@require_POST
@teacher_required
def delete_category(request, subject_id):
    pass
    #Todo Marek View+Html

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
