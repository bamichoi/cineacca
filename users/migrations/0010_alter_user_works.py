# Generated by Django 3.2.5 on 2021-11-10 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20211103_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='works',
            field=models.ManyToManyField(blank=True, related_name='users', to='users.Work'),
        ),
    ]
