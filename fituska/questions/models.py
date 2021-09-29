from django.db import models

from accounts.model import User


class Rating(models.Model):

    type = models.BooleanField('type')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)


class Answer(models.Model):
    pass
