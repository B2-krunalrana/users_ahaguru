# Generated by Django 4.1.3 on 2022-11-27 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usersapp', '0003_rename_users_users_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users_data',
            name='number',
            field=models.CharField(max_length=80),
        ),
    ]
