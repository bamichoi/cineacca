# Generated by Django 3.2.5 on 2021-11-22 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0019_auto_20211121_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='team',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='truppe'),
        ),
    ]
