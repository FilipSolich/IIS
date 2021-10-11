from django.forms import ModelForm
from .models import Subject


class AddSubjectForm(ModelForm):

    class Meta:

        model = Subject
        fields = ('name', 'year')
