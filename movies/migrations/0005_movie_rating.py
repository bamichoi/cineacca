# Generated by Django 3.2.5 on 2021-11-02 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movie_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]