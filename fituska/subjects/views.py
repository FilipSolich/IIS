from django.shortcuts import render


def list_subjects(request):
    return render(request, 'subjects/subjects.html')
