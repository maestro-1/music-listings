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


DUMMY_RESPONSE = 'The track "Home" by Bethel Music, with a track rating of 39 and 5 favorites, is from the album "We Will Not Be Shaken" and falls under the primary genre of "Praise & Worship" in the Christian & Gospel category.'


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
            return "This song could not be found"

        track_id = song.get("track_id")
        if track_id is None:
            return SongDetail(summary=None, country_list=None)

        lyrics_params = {
            "track_id": track_id,
            "apikey": settings.MUSIX_API_KEY,
        }
        lyrics = retrieve_lyrics(session, lyrics_params)

    if lyrics is None:
        return SongDetail(summary=None, country_list=None)

    client = OpenAI(
        api_key=settings.OPENAI_API_KEY,
    )
    song_summary = summarize_song(client.completions, lyrics)
    country_list = list_countries_in_song(client.completions, song)

    disallowed_list = ["None"]
    if len(re.findall(r"(?=(" + "|".join(disallowed_list) + r"))", country_list)) > 0:
        country_list = ""

    return SongDetail(song_summary, country_list)
