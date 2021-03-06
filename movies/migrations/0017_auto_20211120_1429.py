# Generated by Django 3.2.5 on 2021-11-20 05:29

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0016_movie_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='casting',
            field=models.CharField(max_length=300, verbose_name='attori'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(max_length=1000, verbose_name='sinossi'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=300, null=True, verbose_name='regia'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='editor',
            field=models.CharField(max_length=300, verbose_name='montaggio'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='makeup_artist',
            field=models.CharField(max_length=300, verbose_name='make-up artist'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='screenwriter',
            field=models.CharField(max_length=300, verbose_name='sceneggiatura'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1900)], verbose_name='anno'),
        ),
        migrations.CreateModel(
            name='VideoArts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('video', models.FileField(blank=True, null=True, upload_to='movie_files')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='movie_thumbnails', verbose_name='thumbnail')),
                ('title', models.CharField(max_length=300, verbose_name='titolo')),
                ('description', models.TextField(max_length=1000, verbose_name='sinossi')),
                ('year', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1900)], verbose_name='anno')),
                ('views', models.IntegerField(default=0)),
                ('director', models.CharField(max_length=300, null=True, verbose_name='regia')),
                ('screenwriter', models.CharField(max_length=300, verbose_name='sceneggiatura')),
                ('casting', models.CharField(max_length=300, verbose_name='attori')),
                ('editor', models.CharField(max_length=300, verbose_name='montaggio')),
                ('director_of_photograpy', models.CharField(max_length=300, verbose_name='fotografia')),
                ('audio_director', models.CharField(max_length=300, verbose_name='audio')),
                ('music', models.CharField(max_length=300, verbose_name='musica')),
                ('art_director', models.CharField(max_length=300, verbose_name='scenografia')),
                ('costume_designer', models.CharField(max_length=300, verbose_name='costume')),
                ('makeup_artist', models.CharField(max_length=300, verbose_name='make-up artist')),
                ('spacial_effect_supervisor', models.CharField(max_length=300, verbose_name='effetto speciale')),
                ('sound_designer', models.CharField(max_length=300, verbose_name='sound')),
                ('rating', models.FloatField(default=0.0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videoarts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
