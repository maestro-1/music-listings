from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MusicDetails(models.Model):
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=100)
    listed_countries = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

