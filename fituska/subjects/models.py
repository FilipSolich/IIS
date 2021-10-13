from django.db import models

from accounts.models import User


class Category(models.Model):
    pass


class Subject(models.Model):
    class choice_compulsory(models.TextChoices):
        compulsory = 'povinný'
        uncompulsory = 'nepovinný'

    class type_semester(models.TextChoices):
        winter = "zimní"
        summer = "letní"

    name = models.CharField('Nazev předmětu', max_length=100, unique=True, null=True)
    year = models.IntegerField('Ročník', null=True)
    semester = models.CharField('Semestr(Z/L)',max_length=20, null=True)
    shortcut = models.CharField('Short name of subject', max_length=6,choices = type_semester.choices, null = True ,blank = False)
    grade = models.IntegerField('Year of study', null = True ,blank = False) #after database data change null to False !!! #TODO
    compulsory = models.CharField(max_length=20,choices=choice_compulsory.choices, default=choice_compulsory.uncompulsory)

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
