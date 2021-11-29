import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from users.models import User, Work


class Command(BaseCommand):

    help = "This command create many fake users."

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="how many users do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(
            User,
            number,
            {
                "account_type": "student",
                "is_staff": False,
                "is_superuser": False,
                "email_verified": False,
            },
        )
        created_users = (
            seeder.execute()
        )  # {<class 'users.models.User'>: [359, 360]} <class 'dict'>
        cleaned_user = flatten(list(created_users.values()))
        # dict_values([[359, 360]]) <class 'dict_values'>
        # [[359, 360]] <class 'list'>
        # [359, 360] <class 'list'>
        print(cleaned_user, type(cleaned_user))
        works = Work.objects.all()
        for pk in cleaned_user:
            user = User.objects.get(pk=pk)
            for work in works:
                ran_number = random.randint(1, 15)
                if ran_number % 2 == 0:
                    user.works.add(work)
        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))
