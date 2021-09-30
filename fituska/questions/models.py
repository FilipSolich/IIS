from django.db import models

from accounts.models import User
from subjects.models import Category, Subject


class Question(models.Model):

    title = models.CharField('title', max_length=150)
    text = models.TextField('text', max_length=10000)
    picture = models.ImageField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class AbstractAnswer(models.Model):

    text = models.TextField(blank=False, max_length=10000)
    picture = models.ImageField(blank=True)

    class Meta:
        abstract = True


class Answer(AbstractAnswer):

    validity = models.BooleanField('type',blank=True)
    points = models.DecimalField(max_digits=5,decimal_places=0, blank=True)
    teacher_points = models.DecimalField(max_digits=5,decimal_places=0,blank=True)

    user = models.ForeignKey(User, on_delete=models.PROTECT) # can be cascade
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class Reaction(AbstractAnswer):

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)


class Rating(models.Model):

    type = models.BooleanField('type')

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
