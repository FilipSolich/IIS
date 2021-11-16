from django.contrib.auth.decorators import login_required, permission_required
from django.http import response, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import Subject, Category, Registration
from .forms import AddSubjectForm, ConfirmSubjectForm, FilterYearForm, AddCategoryForm, RegisterSubjectForm
from accounts.models import User
from accounts.decorators import teacher_required
from utils import get_unique_values, get_current_school_year


def list_subjects(request):
    subjects = Subject.objects.filter(confirmed=True)
    years = get_unique_values(subjects, '-year')
    current_year = get_current_school_year()
    if not current_year in years:
        years.insert(0, current_year)

    form = FilterYearForm(request.GET, years=years, default_none=False)

    year = request.GET.get('year')
    if not year or year == '--':
        year = current_year
    subjects = subjects.filter(year=year)

    compulsory = get_unique_values(subjects, 'compulsory')
    grade = get_unique_values(subjects, 'grade')
    semester = get_unique_values(subjects, '-semester')

    subjects_dict = {c: {g: {s: [] for s in semester} for g in grade} for c in compulsory}

    for subject in subjects:
        subjects_dict[subject.compulsory][subject.grade][subject.semester].append(subject)

    return render(request, 'subjects/subjects.html', {
        'subjects_dict': subjects_dict,
        'form': form,
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
    unconfirmed_subjects = Subject.objects.filter(confirmed=None)
    return render(request, 'subjects/unconfirmed.html', {'unconfirmed_subjects': unconfirmed_subjects})

@permission_required('subjects.can_confirm_subject')
def confirm_subject(request, subject_id):
    subject = Subject.objects.get(id = subject_id)
    if request.method == 'POST':
        
        form = ConfirmSubjectForm(request.POST, instance=subject)

        if form.is_valid():
            subject.confirmed = True
            subject = form.save()
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
    subject = get_object_or_404(Subject, pk = subject_id)
    category = Category.objects.all()
    category = category.filter(subject = subject_id )
    if request.method == 'POST':
        form = AddCategoryForm(request.POST)
        if form.is_valid():
            cat = form.save(commit = False)
            cat.subject_id = subject_id
            cat.save()
            return redirect('create_category', subject_id = subject_id)
    else:
        form = AddCategoryForm()
    return render(request, 'subjects/new_category.html', {'category': category,'form': form ,'subject': subject})

@require_POST
@teacher_required
def delete_category(request, subject_id):
    get_object_or_404(Category, pk=request.POST.get('category_id')).delete()
    return redirect('create_category', subject_id = subject_id)

@teacher_required
def students(request, subject_id):
    students_list = []
    for user in User.objects.all():
        if(user.is_student(subject_id)):
            students_list.append(user)
    
    return render(request, 'subject/students.html', {'students_list':students_list,})


@require_POST
@teacher_required
def confirm_student(request, subject_id):
    pass


@require_POST
@teacher_required
def reject_student(request, subject_id):
    pass


#@require_POST
@login_required
def register_subject(request, subject_id):
    subject = Subject.objects.get(id = subject_id)

    if request.method == 'POST':
        form = RegisterSubjectForm(request.POST)
        if form.is_valid():
            registration = form.save(commit = False)
            registration.confirmed = None
            registration.user = request.user
            registration.subject = Subject.objects.get(pk=subject_id)
            registration.save()
        return redirect("/")
    else:
        form = RegisterSubjectForm()
    return render(request, 'subjects/register_subject.html', {'subject':subject, 'form': form})
