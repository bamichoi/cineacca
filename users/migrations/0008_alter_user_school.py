# Generated by Django 3.2.5 on 2021-10-05 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='school',
            field=models.CharField(blank=True, choices=[('Acccademia belle Arti di roma', 'Accademia Belle Arti di Roma')], max_length=50, null=True, verbose_name='accademia'),
        ),
    ]
