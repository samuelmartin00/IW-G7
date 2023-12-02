from django.db import models
from django_cleanup import cleanup

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Artist(models.Model):
    name = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='artist_images/', null=True, blank=True)
    description = models.TextField(blank=True)  # Added description field

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    year = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
    duration = models.DurationField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='song_audio/', null=True, blank=True)
    description = models.TextField(blank=True)
    lyrics = models.TextField(blank=True)

    @property
    def audio_url(self):
        if self.audio_file and hasattr(self.audio_file, 'url'):
            return self.audio_file.url
        return ''