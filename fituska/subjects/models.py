from django.db import models

from accounts.models import User


class Category(models.Model):
    pass


class Subject(models.Model):

    name = models.CharField('Nazev předmětu', max_length=100, unique=True, null=True)
    year = models.IntegerField('Ročník', null=True)
    semester = models.CharField('Semestr(Z/L)',max_length=20, null=True)

    class Meta:
        permissions = (
            ('can_confirm_subject', 'Can confirm subject'),
        )

    def __str__(self):
        return self.name

class Registration(models.Model):

    confirmed = models.BooleanField('confirm', null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
