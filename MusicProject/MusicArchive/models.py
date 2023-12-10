from django.db import models
from django_cleanup import cleanup
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='artist_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='artist_images/', null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    album = models.ForeignKey('Album', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='song_images/', null=True, blank=True)
    duration = models.DurationField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='song_audio/', null=True, blank=True)
    description = models.TextField(blank=True)
    lyrics = models.TextField(blank=True)
    
    def __str__(self):
        return self.title

def get_song_audio_file_path(instance, filename):
    album_id = instance.album.id if instance.album else 'no_album'
    return f'song_audio/{album_id}/{filename}'

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    year = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='album_images/', blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def delete(self, using=None, keep_parents=False):
        for song in self.songs.all():
            song.delete()
        super().delete(using=using, keep_parents=keep_parents)

class Satisfaction(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=255)
    rating = models.IntegerField()

    @property
    def audio_url(self):
        if self.audio_file and hasattr(self.audio_file, 'url'):
            return self.audio_file.url
        return ''