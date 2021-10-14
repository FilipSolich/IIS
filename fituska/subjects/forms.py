from django import forms
from django.forms import ModelForm

from .models import Subject

class AddSubjectForm(ModelForm):

    class Meta:

        model = Subject
        fields = '__all__'


class FilterYearForm(forms.Form):

    def __init__(self, *args, **kwargs):
        years = kwargs.pop('years')

        super().__init__(*args, **kwargs)

        years = [(year, year) for year in years]
        years.insert(0, ('--', '--'))
        self.fields['year'] = forms.ChoiceField(choices=years, required=False)
