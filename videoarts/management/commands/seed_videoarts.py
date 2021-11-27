import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from videoarts.models import VideoArt
from users.models import User


class Command(BaseCommand):

    help = "This command create many fake video arts."

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="how many video arts do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = User.objects.all()
        seeder.add_entity(
            VideoArt,
            number,
            {
                "video": lambda x: f"/videoart_files/{random.randint(1, 6)}.mov",
                "thumbnail": lambda x: f"/videoart_thumbnails/{random.randint(1, 6)}.jpeg",
                "year": lambda x: random.randint(1900, 2022),
                "views": 0,
                "rating": 0,
                "user": lambda x: random.choice(all_users),
                "artist": lambda x: seeder.faker.name(),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} videoarts created!"))
