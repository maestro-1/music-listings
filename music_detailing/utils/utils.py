from dataclasses import dataclass
import re

from openai import OpenAI
import requests

from django.conf import settings
from .http_utils import (
    retrieve_song,
    summarize_song,
    list_countries_in_song,
    retrieve_lyrics,
)

@dataclass
class SongDetail:
    summary: str
    country_list: str


def generate_song_details(artist_name: str, title: str):
    song_params = {
        "q_artist": artist_name,
        "q_track": title,
        "apikey": settings.MUSIX_API_KEY,
    }
    with requests.session() as session:
        song = retrieve_song(session, song_params)

        if song is None:
            return (None, None)

        track_id = song.get("has_lyrics")
        if track_id == 0:
            return (song, None)

        lyrics_params = {
            "track_id": track_id,
            "apikey": settings.MUSIX_API_KEY,
        }
        lyrics = retrieve_lyrics(session, lyrics_params)

    if lyrics is None:
        return (song, None)

    return (song, lyrics)


def generate_song_summary(lyrics: str):
    client = OpenAI(
        api_key=settings.OPENAI_API_KEY,
    )
    song_summary = summarize_song(client.completions, lyrics)
    country_list = list_countries_in_song(client.completions, lyrics)

    disallowed_list = ["None"]
    if len(re.findall(r"(?=(" + "|".join(disallowed_list) + r"))", country_list)) > 0:
        country_list = ""

    return SongDetail(song_summary, country_list)
