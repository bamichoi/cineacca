# Generated by Django 3.2.5 on 2021-11-26 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0027_alter_movie_makeup_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='edition_secretary',
            field=models.CharField(blank=True, max_length=300, verbose_name='segretaria di edizione'),
        ),
        migrations.AddField(
            model_name='movie',
            name='phonic',
            field=models.CharField(blank=True, max_length=300, verbose_name='foico di presa diretta'),
        ),
    ]
