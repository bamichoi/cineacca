# Generated by Django 3.2.5 on 2021-11-22 07:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0022_auto_20211122_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='fav',
            field=models.ManyToManyField(related_name='fav_movies', to=settings.AUTH_USER_MODEL),
        ),
    ]
