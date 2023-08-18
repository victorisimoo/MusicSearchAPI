from django.db import models

# Create your models here.


class Song(models.Model):
    name = models.CharField(max_length=255)
    song_id = models.CharField(max_length=255, unique=True)
    album = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album_cover = models.URLField()
    year_release_date = models.CharField(max_length=4)
    genres = models.JSONField()
    duration = models.DurationField()
    origin = models.CharField(max_length=255)
