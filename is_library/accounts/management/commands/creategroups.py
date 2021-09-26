from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **oprtions):
        librarians = Group(name='Librarians')
        book_distributors = Group(name='Book distributors')

        librarians.save()
        book_distributors.save()
