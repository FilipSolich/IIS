from django import forms

from .models import Question


# TODO add category option
class QuestionForm(forms.ModelForm):

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
