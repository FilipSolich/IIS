from django.db import models


class Subject(models.Model):

    from accounts.models import User

    class CompulsoryChoice(models.TextChoices):

        COMPULSORY = 'compulsory', 'Povinný'
        UNCOMPULSORY = 'uncompulsory', 'Nepovinný'

    class SemesterType(models.TextChoices):

        WINTER = 'winter', 'Zimní'
        SUMMER = 'summer', 'Letní'

    name = models.CharField(max_length=100, blank=False, null=False)
    shortcut = models.CharField(max_length=6, blank=False, null=False)
    year = models.IntegerField(blank=False, null=False)
    semester = models.CharField(max_length=20, choices=SemesterType.choices, default=SemesterType.WINTER, blank=False, null=False)
    grade = models.IntegerField(blank=False, null=False)
    compulsory = models.CharField(max_length=20, choices=CompulsoryChoice.choices, default=CompulsoryChoice.UNCOMPULSORY)
    confirmed = models.BooleanField(default=False, null=False)

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

    from accounts.models import User

    confirmed = models.BooleanField(null=True, default=None)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class Category(models.Model):

    name = models.CharField(max_length=100, blank=False, null=False)

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
