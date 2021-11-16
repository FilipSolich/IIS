from django import forms
from django.forms import ModelForm, BooleanField

from .models import Subject
from .models import Category


class AddSubjectForm(ModelForm):

    class Meta:

        model = Subject
        fields = ['name', 'shortcut', 'year', 'semester', 'grade', 'compulsory']


class ConfirmSubjectForm(ModelForm):

    class Meta:

        model = Subject
        fields = ['confirmed',]


class FilterYearForm(forms.Form):

    def __init__(self, *args, **kwargs):
        years = kwargs.pop('years')
        default_none = kwargs.pop('default_none', True)

        super().__init__(*args, **kwargs)

        years = [(year, f'{year}/{year+1}') for year in years]
        if default_none:
            years.insert(0, ('--', '--'))
        self.fields['year'] = forms.ChoiceField(choices=years, required=False)


class AddCategoryForm(ModelForm):

    class Meta:

        model = Category
        fields = ['name',]
