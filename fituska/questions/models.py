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

    class Meta:

        ordering = ('-id',)

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

    valid = models.BooleanField('valid', blank=True, null=True)
    teacher_points = models.IntegerField('teacher_points', default=0, blank=True)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    @property
    def points(self):
        ratings = [rating.type for rating in Rating.objects.filter(answer=self)]
        return ratings.count(True) - ratings.count(False)

    @property
    def sum_points(self):
        return self.points + self.teacher_points


class Reaction(AbstractAnswer):

    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)


class Rating(models.Model):

    type = models.BooleanField('type')

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
