# Generated by Django 3.2.5 on 2021-11-27 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0032_alter_movie_assistant_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='assistant_director',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='aiuto regia'),
        ),
    ]
