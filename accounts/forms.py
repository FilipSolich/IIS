from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django import forms

from .models import User
from subjects.forms import FilterYearForm


class UserCreationForm(BaseUserCreationForm):

    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'email@domain.cz'}))
    login = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'xsechr00'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Jan'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Novák'}))

    class Meta:

        model = User
        fields = ('email', 'login', 'first_name', 'last_name')


class FilterLeaderboardForm(forms.Form):

    def __init__(self, *args, **kwargs):
        subjects = kwargs.pop('subjects')

        super().__init__(*args, **kwargs)

        subjects_choices = [
            (f'{subject.id}', f'{subject.school_year} {subject.shortcut}') for subject in subjects
        ]
        subjects_choices.insert(0, ('--', '--'))
        self.fields['subject'] = forms.ChoiceField(
            choices=subjects_choices, required=False, label='Předmět'
        )
