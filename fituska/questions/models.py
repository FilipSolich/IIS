from django.db import models

from accounts.models import User

class Answer(models.Model):
    pass

class Rating(models.Model):

    type = models.BooleanField('type')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)



