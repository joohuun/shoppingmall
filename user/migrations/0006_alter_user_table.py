# Generated by Django 4.0.5 on 2022-06-27 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_profile_user'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='유저',
        ),
    ]