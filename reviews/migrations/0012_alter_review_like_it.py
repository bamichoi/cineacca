# Generated by Django 3.2.5 on 2021-11-24 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_alter_review_like_it'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='like_it',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
