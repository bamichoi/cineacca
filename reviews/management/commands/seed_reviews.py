import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User
from movies.models import Movie
from reviews.models import Review


class Command(BaseCommand):

    help = "This command create many fake reviews."

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="how many reviews do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        all_user = User.objects.all()
        all_movie = Movie.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(
            Review,
            number,
            {
                "user": lambda x: random.choice(all_user),
                "movie": lambda x: random.choice(all_movie),
                "rate": lambda x: random.randint(1, 5),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reviews created!"))
