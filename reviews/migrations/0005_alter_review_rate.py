# Generated by Django 3.2.5 on 2021-11-16 07:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_alter_review_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
    ]
