from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        perm = Permission.objects.get(codename='can_confirm_subject')
        group, _ = Group.objects.get_or_create(name='Moderators')
        group.permissions.add(perm)
        group.save()
