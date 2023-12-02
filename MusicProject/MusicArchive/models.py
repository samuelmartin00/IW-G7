from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Artist(models.Model):
    name = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='artist_images/', null=True, blank=True)  # Define the ImageField

    def __str__(self):
        return self.name
    # Agrega otros campos relevantes para el artista

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    year = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    # Agrega otros campos relevantes para el álbum

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)  # nullable field
    duration = models.DurationField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    # Agrega otros campos relevantes para la canción
