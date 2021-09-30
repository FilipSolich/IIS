from django.db import models

from accounts.model import User
from subjects.models import Category, Subject


class Question(models.Model):

    title = models.CharField('title', max_length=150)
    text = models.TextField('text', max_length=10000)
    picture = models.ImageField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Rating(models.Model):

    type = models.BooleanField('type')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)


class Answer(models.Model):
    pass
