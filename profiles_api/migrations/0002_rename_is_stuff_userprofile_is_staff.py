# Generated by Django 4.2 on 2024-08-30 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_stuff',
            new_name='is_staff',
        ),
    ]
