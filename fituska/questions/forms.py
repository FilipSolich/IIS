from django import forms

from .models import Question
from subjects.models import Category


class QuestionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        subject = kwargs.pop('subject')

        super().__init__(*args, **kwargs)

        self.fields['category'] = forms.ModelChoiceField(
            queryset=Category.objects.filter(subject=subject)
        )

    class Meta:

        model = Question
        fields = ['title', 'text', 'picture', 'category']


class ConfirmAnswerForm(forms.Form):

    teacher_points = forms.IntegerField(initial=0)
    answer_id = forms.IntegerField(widget=forms.HiddenInput())

    def clean_teacher_points(self):
        value = self.cleaned_data['teacher_points']
        if value < 0:
            raise ValidationError('Body musí být kladné číslo.')

        return value


class FilterCategoryForm(forms.Form):

    def __init__(self, *args, **kwargs):
        subject = kwargs.pop('subject')

        super().__init__(*args, **kwargs)

        category = [
            (category.id, category.name) for category in Category.objects.firlter(subject=subject)
        ]
        category.insert(0, ('--', '--'))
        self.fields['category'] = forms.ChoiceField(choices=category, required=False)
