from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from subjects.models import Subject


class User(AbstractBaseUser, PermissionsMixin):

    login = models.CharField('login', max_length=8, unique=True)
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('first name', max_length=150, blank=True)
    last_name = models.CharField('last name', max_length=150, blank=True)

    subjects = models.ManyToManyField(Subject)

    USERNAME_FIELD = 'login'

    def __str__(self):
        return self.login

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    @property
    def karma(self):
        all_karma = Karma.objects.filter(user=self)
        all_karma = [int(karma) for karma in all_karma]
        return sum(all_karma)

    @property
    def is_moderator(self):
        return self.groups.filter(name='Moderators').exist()


class Karma(models.Model):

    karma = models.IntegerField('karma', default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

    def __int__(self):
        return self.karma
