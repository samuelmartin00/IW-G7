# Generated by Django 4.2.6 on 2023-12-10 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MusicArchive', '0011_album_songs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='songs',
        ),
    ]
