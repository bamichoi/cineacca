# Generated by Django 3.2.5 on 2021-11-24 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoarts', '0007_videoart_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoart',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='videoart_posters', verbose_name='locandina'),
        ),
    ]
