# Generated by Django 4.1.3 on 2022-11-28 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_library', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Music_Library',
            new_name='Song',
        ),
    ]
