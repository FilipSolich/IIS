from django.shortcuts import render

# Create your views here.
def temple_questions(request):
    return render(request,"questions/questions.html")

