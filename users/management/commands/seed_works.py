from django.core.management.base import BaseCommand
from users.models import Work


class Command(BaseCommand):

    help = "This command creates works."

    def handle(self, *args, **options):
        works = [
            "regia",
            "sceneggiatura",
            "recitazione",
            "fotografia",
            "montaggio",
            "VFX",
            "audio",
            "scenografia",
            "costume",
            "truccatura",
            "musica",
        ]
        for work in works:
            Work.objects.create(name=work)
        self.stdout.write(self.style.SUCCESS("Works created!"))
