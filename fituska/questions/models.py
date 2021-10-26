from django.db import models

from accounts.models import User
from subjects.models import Category, Subject


class Question(models.Model):

    title = models.CharField('title', max_length=150)
    text = models.TextField('text', max_length=10000, blank=True, null=True)
    picture = models.ImageField('picture', blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class AbstractAnswer(models.Model):

    text = models.TextField(blank=False, max_length=10000)
    picture = models.ImageField('picture', blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        abstract = True

    def __str__(self):
        return self.text


class Answer(AbstractAnswer):

    validity = models.BooleanField('validity', blank=True, null=True)
    points = models.DecimalField('points', max_digits=5, decimal_places=0, blank=True, default=0)
    teacher_points = models.DecimalField('teacher_points', max_digits=5, decimal_places=0, default=0, blank=True)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    @property
    def sum_points(self):
        return self.points + self.teacher_points

    def add_points(self, type_, value=1):
        if type_:
            self.points += value
        else:
            self.points -= value

        self.save()


class Reaction(AbstractAnswer):

    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)


class Rating(models.Model):

    type = models.BooleanField('type')

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
