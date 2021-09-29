from django.db import models

from accounts.models import User

class Answer(models.Model):

    text = models.TextField(blank=False,max_length=10000)
    picture = models.ImageField(blank=True)
    validity = models.BooleanField('type',blank=True)
    points = models.DecimalField(max_digits=5,decimal_places=0, blank=True)
    teacher_points = models.DecimalField(max_digits=5,decimal_places=0,blank=True)

    user = models.ForeignKey(User, on_delete=models.PROTECT) # can be cascade
    #question = models.ForeignKey(Question, on_delete=models.CASCADE)


class Reaction(models.Model):

    text = models.TextField(blank=False,max_length=10000)
    picture = models.ImageField(blank=True)

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)


class Rating(models.Model):

    type = models.BooleanField('type')

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)



