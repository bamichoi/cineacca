# Generated by Django 3.2.5 on 2021-12-12 11:21

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20211126_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(default='user_avatars/default_avatar.jpeg', upload_to='user_avatars'),
        ),
    ]
