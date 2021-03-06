# Generated by Django 3.2.5 on 2021-09-16 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='movie_files')),
                ('thumnail', models.ImageField(blank=True, null=True, upload_to='movie_thumnails', verbose_name='locandina')),
                ('title', models.CharField(max_length=300, verbose_name='titolo')),
                ('description', models.TextField(max_length=1000, verbose_name='descrizione')),
                ('director', models.CharField(max_length=300, null=True, verbose_name='regista')),
                ('screenwriter', models.CharField(max_length=300, verbose_name='sceneggiatore')),
                ('casting', models.CharField(max_length=300)),
                ('editor', models.CharField(max_length=300, verbose_name='montatore')),
                ('director_of_photograpy', models.CharField(max_length=300, verbose_name='fotografia')),
                ('audio_director', models.CharField(max_length=300, verbose_name='audio')),
                ('music', models.CharField(max_length=300, verbose_name='musica')),
                ('art_director', models.CharField(max_length=300, verbose_name='scenografia')),
                ('costume_designer', models.CharField(max_length=300, verbose_name='costume')),
                ('makeup_artist', models.CharField(max_length=300, verbose_name='make-up artista')),
                ('spacial_effect_supervisor', models.CharField(max_length=300, verbose_name='effetto speciale')),
                ('sound_designer', models.CharField(max_length=300, verbose_name='sound')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
