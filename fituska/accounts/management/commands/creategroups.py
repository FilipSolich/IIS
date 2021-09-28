from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        mod = Group.objects.create(name='Moderators')
        mod.save()
