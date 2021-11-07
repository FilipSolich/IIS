from django.db import models

from accounts.models import User


class Subject(models.Model):

    class CompulsoryChoice(models.TextChoices):

        COMPULSORY = 'povinny', 'Povinný'
        UNCOMPULSORY = 'nepovinny', 'Nepovinný'

    class SemesterType(models.TextChoices):

        WINTER = 'zimní', 'Zimní'
        SUMMER = 'letní', 'Letní'

    name = models.CharField(max_length=100, blank=False, null=False)
    shortcut = models.CharField(max_length=6, blank=False, null=False)
    year = models.IntegerField(blank=False, null=False)
    semester = models.CharField(max_length=20, choices=SemesterType.choices, default=SemesterType.WINTER, blank=False, null=False)
    grade = models.IntegerField(blank=False, null=False)
    compulsory = models.CharField(max_length=20, choices=CompulsoryChoice.choices, default=CompulsoryChoice.UNCOMPULSORY)
    confirmed = models.BooleanField(null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:

        permissions = (
            ('can_confirm_subject', 'Can confirm subject'),
        )

    def __str__(self):
        return self.name

    @property
    def school_year(self):
        return f'{self.year}/{self.year+1}'


class Registration(models.Model):

    confirmed = models.BooleanField(null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class Category(models.Model):

    name = models.CharField(max_length=100, blank=False, null=False)

    subject = models.ForeignKey(Subject, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
