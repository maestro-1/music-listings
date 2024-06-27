from unittest.mock import Mock, patch, MagicMock
from django.conf import settings
from requests import Session

from .utils import request_song, request_lyrics, request_non_existent_song, request_no_lyrics, request_song_without_lyrics
from ..utils.utils import generate_song_details
from .mocked_data import (
    song,
    lyrics,
    song_without_lyrics
)


@patch.object(Session, "get")
def test_song_and_lyrics_exists(mock_get):
    mock_get.side_effect = [request_song(), request_lyrics()]

    (response1, response2) = generate_song_details("Bethel Music", "Goodness of God")

    assert response1 == song
    assert response2 == lyrics
    assert mock_get.call_count == 2


@patch.object(Session, "get")
def test_song_does_not_exists(mock_get):
    mock_get.side_effect = [request_non_existent_song(), request_lyrics()]

    (response1, _) = generate_song_details("Benjamin Goodman", "Havilla")

    assert response1 == None
    assert mock_get.call_count == 1


@patch.object(Session, "get")
def test_lyrics_does_not_exists(mock_get):
    mock_get.side_effect = [request_song(), request_no_lyrics()]

    (response1, response2) = generate_song_details("Bethel Music", "Goodness of God")
    assert response1 == song
    assert response2 == None
    assert mock_get.call_count == 2


@patch.object(Session, "get")
def test_song_without_lyrics(mock_get):
    mock_get.side_effect = [request_song_without_lyrics()]

    (response1, response2) = generate_song_details("Bethel Music", "Goodness of God")

    assert response1 == song_without_lyrics["message"]["body"]["track_list"][0]["track"]
    assert response2 == None
    assert mock_get.call_count == 1
