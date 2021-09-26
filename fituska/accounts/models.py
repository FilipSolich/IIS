from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.first_name

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
