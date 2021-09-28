from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):

    login = models.CharField('login', max_length=8, unique=True)
    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('first name', max_length=150, blank=True)
    last_name = models.CharField('last name', max_length=150, blank=True)
    karma = models.IntegerField('karma', default=0)

    USERNAME_FIELD = 'login'

    def __str__(self):
        return self.login

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
