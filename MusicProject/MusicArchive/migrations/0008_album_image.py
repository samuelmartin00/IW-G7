# Generated by Django 4.2.6 on 2023-12-09 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicArchive', '0007_satisfaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='album_images/'),
        ),
    ]
