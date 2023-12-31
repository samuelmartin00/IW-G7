# Generated by Django 4.2.6 on 2023-12-02 13:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MusicArchive', '0005_song_audio_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='song',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='song',
            name='lyrics',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='MusicArchive.artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='MusicArchive.artist'),
        ),
    ]
