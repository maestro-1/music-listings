from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    country_list = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
