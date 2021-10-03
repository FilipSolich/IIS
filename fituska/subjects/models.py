from django.db import models


class Category(models.Model):
    pass


class Subject(models.Model):

    class Meta:
        permissions = (
            ('can_confirm_subject', 'Can confirm subject'),
        )
