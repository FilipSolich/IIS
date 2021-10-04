from django.db import models

from accounts.models import User


class Category(models.Model):
    pass


class Subject(models.Model):

    class Meta:
        permissions = (
            ('can_confirm_subject', 'Can confirm subject'),
        )


class Registration(models.Model):

    confirmed = models.BooleanField('confirm', null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
