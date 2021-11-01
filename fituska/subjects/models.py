from django.db import models

from accounts.models import User


class Subject(models.Model):

    class choice_compulsory(models.TextChoices):

        compulsory = 'povinný'
        uncompulsory = 'nepovinný'

    class type_semester(models.TextChoices):

        winter = "zimní"
        summer = "letní"

    name = models.CharField('Nazev předmětu', max_length=100, null=True)
    shortcut = models.CharField('Zkratka předmětu', max_length=6, null=True, blank=False)
    year = models.IntegerField('Rok', null=True)
    semester = models.CharField('Semestr', choices = type_semester.choices, max_length=20, null=True)
    grade = models.IntegerField('Ročník', null=True, blank=False) #after database data change null to False !!! #TODO
    compulsory = models.CharField(max_length=20, choices=choice_compulsory.choices, default=choice_compulsory.uncompulsory)
    confirmed = models.BooleanField('Schválit předmět', null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

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


class Category(models.Model):

    name = models.CharField('category_name', max_length=100, null=True)

    subject = models.ForeignKey(Subject, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
