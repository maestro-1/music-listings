from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=50)
    summary = models.TextField()
    artist = models.CharField(max_length=50)
    country_list = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
