from typing import Any
from django.contrib import admin, messages
from django.forms import ModelForm

from .utils.utils import generate_song_details, generate_song_summary
from .models import Song


class AddSongForm(ModelForm):
    class Meta:
        model = Song
        fields = ["artist", "title"]


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    form = AddSongForm
    list_display = ["title", "summary", "artist", "country_list"]

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        content = AddSongForm(request.POST)
        if content.is_valid():
            song_title = content.cleaned_data["title"]
            artist = content.cleaned_data["artist"]

        (song, lyrics) = generate_song_details(artist, song_title)

        if song is None:
            return messages.error(request, "Song could not be found")
        
        if lyrics is None:
            messages.error(request, "Could not get the lyrics for this song")

        summary_details = generate_song_summary(lyrics)
        obj.title = song_title
        obj.artist = artist
        obj.summary = summary_details.summary
        obj.country = summary_details.country_list

        return super().save_model(request, obj, form, change)
