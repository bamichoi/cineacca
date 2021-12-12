import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users.models import User


class Command(BaseCommand):

    help = "This command create superuser."

    def handle(self, *args, **options):
        try:
            User.objects.get(email="admin@cineacca.it")
        except User.DoesNotExist:
            User.objects.create_superuser("admin@cineacca.it", "cineacca1283")
            return self.stdout.write(self.style.SUCCESS("superuser created!"))
            
        return self.stdout.write(self.style.SUCCESS("superuser exists."))