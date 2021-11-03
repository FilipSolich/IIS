from django.db import models

from accounts.models import User


class Subject(models.Model):

    class choice_compulsory(models.TextChoices):

        compulsory = 'povinný'
        uncompulsory = 'nepovinný'

    class type_semester(models.TextChoices):

        winter = "zimní"
        summer = "letní"

    name = models.CharField(max_length=100, blank=False, null=False)
    shortcut = models.CharField(max_length=6, blank=False, null=False)
    year = models.IntegerField(blank=False, null=False)
    semester = models.CharField(choices=type_semester.choices, max_length=20, blank=False, null=False)
    grade = models.IntegerField(blank=False, null=False)
    compulsory = models.CharField(max_length=20, choices=choice_compulsory.choices, default=choice_compulsory.uncompulsory)
    confirmed = models.BooleanField(null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:

        permissions = (
            ('can_confirm_subject', 'Can confirm subject'),
        )

    def __str__(self):
        return self.name


class Registration(models.Model):

    confirmed = models.BooleanField(null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class Category(models.Model):

    name = models.CharField(max_length=100, blank=False, null=False)

    subject = models.ForeignKey(Subject, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
