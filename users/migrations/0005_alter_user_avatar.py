# Generated by Django 3.2.5 on 2021-10-04 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='0.jpeg', upload_to='user_avatars'),
        ),
    ]
