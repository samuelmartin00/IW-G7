# Generated by Django 4.2.6 on 2023-12-02 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicArchive', '0004_artist_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='audio_file',
            field=models.FileField(blank=True, null=True, upload_to='song_audio/'),
        ),
    ]
