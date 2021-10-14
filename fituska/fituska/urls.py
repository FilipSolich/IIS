from django.urls import include, path

from subjects.views import list_subjects


# TODO remove
def test_base(request):
    from django.shortcuts import render
    return render(request, "base.html")

urlpatterns = [
    path('', list_subjects, name='list_subjects'),
    path('subjects/', include('subjects.urls')),
    path('accounts/', include('accounts.urls')),
    path('questions/', include('questions.urls')),
    path('test/', test_base),
]

