# Generated by Django 4.0.2 on 2022-06-19 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customers',
            new_name='User_Sign',
        ),
    ]