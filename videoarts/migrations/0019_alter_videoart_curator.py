# Generated by Django 3.2.5 on 2022-01-05 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoarts', '0018_alter_videoart_performer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoart',
            name='curator',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='curatori'),
        ),
    ]
