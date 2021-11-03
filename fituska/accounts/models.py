from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import Group, PermissionsMixin
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):

    login = models.CharField(max_length=8, unique=True, blank=False, null=False)
    email = models.EmailField(unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)

    objects = BaseUserManager()

    USERNAME_FIELD = 'login'

    def __str__(self):
        return self.login

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    @property
    def karma(self):
        all_karma = Karma.objects.filter(user=self)
        return sum([int(karma) for karma in all_karma])

    @property
    def is_moderator(self):
        try:
            self.groups.get(name='Moderators')
            return True
        except Group.DoesNotExist:
            return False

    def is_teacher(self, subject):
        if self.is_superuser:
            return True

        return subject.user == self

    def is_student(self, subject):
        from subjects.models import Registration

        if self.is_superuser:
            return True

        try:
            r = Registration.objects.get(user=self, subject=subject)
            return r.confirmed
        except Registration.DoesNotExist:
            return False


class Karma(models.Model):

    from subjects.models import Subject # Must be here to prevent circular import

    karma = models.IntegerField(default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __int__(self):
        return self.karma
