from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm
from django import forms

from .models import User
from subjects.forms import FilterYearForm


class UserCreationForm(BaseUserCreationForm):

    class Meta:

        model = User
        fields = ('email', 'login', 'first_name', 'last_name')


class FilterLeaderboardForm(FilterYearForm):

    def __init__(self, *args, **kwargs):
        shortcuts = kwargs.pop('shortcuts')

        super().__init__(*args, **kwargs)

        shortcuts = [(shortcut, shortcut) for shortcut in shortcuts]
        shortcuts.insert(0, ('--', '--'))
        self.fields['shortcut'] = forms.ChoiceField(choices=shortcuts, required=False)
