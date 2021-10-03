import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from movies.models import Movie
from users.models import User


class Command(BaseCommand):

    help = "This command create many fake movies."

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="how many movies do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = User.objects.all()
        seeder.add_entity(
            Movie,
            number,
            {
                "video": lambda x: f"/movie_files/{random.randint(1, 6)}.mov",
                "thumnail": lambda x: f"/movie_thumnails/{random.randint(1, 6)}.jpeg",
                "year": lambda x: random.randint(1900, 2022),
                "views": 0,
                "user": lambda x: random.choice(all_users),
                "director": lambda x: seeder.faker.name(),
                "screenwriter": lambda x: seeder.faker.name(),
                "casting": lambda x: seeder.faker.name(),
                "editor": lambda x: seeder.faker.name(),
                "director_of_photograpy": lambda x: seeder.faker.name(),
                "audio_director": lambda x: seeder.faker.name(),
                "music": lambda x: seeder.faker.name(),
                "art_director": lambda x: seeder.faker.name(),
                "costume_designer": lambda x: seeder.faker.name(),
                "makeup_artist": lambda x: seeder.faker.name(),
                "spacial_effect_supervisor": lambda x: seeder.faker.name(),
                "sound_designer": lambda x: seeder.faker.name(),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} movies created!"))
