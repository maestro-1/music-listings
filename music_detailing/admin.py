from typing import Any
from django.contrib import admin, messages
from django.forms import ModelForm

from .utils.utils import generate_song_details
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

        summary_details = generate_song_details(artist, song_title)
        if isinstance(summary_details, str):
            return messages.error(request, summary_details)

        obj.title = song_title
        obj.artist = artist
        obj.summary = summary_details.summary
        obj.country = summary_details.country_list

        return super().save_model(request, obj, form, change)
