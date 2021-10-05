from django.db import models

from accounts.models import User
from subjects.models import Category, Subject


class Question(models.Model):

    title = models.CharField('title', max_length=150)
    text = models.TextField('text', max_length=10000)
    picture = models.ImageField('picture')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class AbstractAnswer(models.Model):

    text = models.TextField(blank=False, max_length=10000)
    picture = models.ImageField(blank=True)

    user = models.ForeignKey(User, on_delete=models.PROTECT)

    class Meta:
        abstract = True


class Answer(AbstractAnswer):

    validity = models.BooleanField('validity', blank=True)
    points = models.DecimalField('points', max_digits=5,decimal_places=0, blank=True)
    teacher_points = models.DecimalField('teacher_points', max_digits=5,decimal_places=0,blank=True)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class Reaction(AbstractAnswer):

    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)


class Rating(models.Model):

    type = models.BooleanField('type')

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
