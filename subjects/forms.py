from django import forms
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ModelForm, BooleanField

from .models import Registration, Subject
from .models import Category


class AddSubjectForm(ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Fyzika II'}))
    shortcut = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'FYZ-02'}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'2021'}))
    grade = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'1'}))

    class Meta:

        model = Subject
        fields = ['name', 'shortcut', 'year', 'semester', 'grade', 'compulsory']

    def clean(self):
        cleaned_data = super().clean()
        shortcut = cleaned_data.get('shortcut')
        year = cleaned_data.get('year')

        try:
            Subject.objects.get(shortcut=shortcut, year=year)
            raise ValidationError('Předmět již existuje')
        except Subject.DoesNotExist:
            pass


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
