from django import forms

from .models import Answer, Question, Reaction
from subjects.models import Category


class QuestionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        subject = kwargs.pop('subject')

        super().__init__(*args, **kwargs)

        self.fields['category'] = forms.ModelChoiceField(
            queryset=Category.objects.filter(subject=subject)
        )
        self.fields['category'].required = False

    class Meta:

        model = Question
        fields = ['title', 'text', 'picture', 'category']


class AnswerForm(forms.ModelForm):

    class Meta:

        model = Answer
        fields = ['text', 'picture']


class ReactionForm(forms.ModelForm):

    answer_id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:

        model = Reaction
        fields = ['text', 'picture']


class QuestionCloseForm(AnswerForm):

    teacher_points = forms.IntegerField(initial=0, required=False)

    def clean_teacher_points(self):
        value = self.cleaned_data['teacher_points']
        if value < 0:
            raise ValidationError('Počet bodů musí být kladné číslo.')

        return value


class FilterCategoryForm(forms.Form):

    def __init__(self, *args, **kwargs):
        subject = kwargs.pop('subject')

        super().__init__(*args, **kwargs)

        category = [
            (category.id, category.name) for category in Category.objects.filter(subject=subject)
        ]
        category.insert(0, ('--', '--'))
        self.fields['category'] = forms.ChoiceField(choices=category, required=False)
