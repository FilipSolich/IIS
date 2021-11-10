from django.db import models

from accounts.models import User
from subjects.models import Category, Subject


class Question(models.Model):

    title = models.CharField(max_length=150, blank=False, null=False)
    text = models.TextField(max_length=10000, blank=True, null=True)
    picture = models.ImageField(blank=True, null=True)
    closed = models.BooleanField(default=False)
    teacher_points = models.IntegerField(default=0, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:

        ordering = ('-id',)

    def __str__(self):
        return self.title


class AbstractAnswer(models.Model):

    text = models.TextField(max_length=10000, blank=False, null=False)
    picture = models.ImageField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:

        abstract = True

    def __str__(self):
        return self.text


class Answer(AbstractAnswer):

    valid = models.BooleanField(default=False)

    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    @property
    def points(self):
        ratings = [rating.type for rating in Rating.objects.filter(answer=self)]
        return ratings.count(True) - ratings.count(False)

    def sum_points(self):
        return self.points + self.question.teacher_points


class Reaction(AbstractAnswer):

    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)


class Rating(models.Model):

    type = models.BooleanField(null=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
