from unittest.mock import Mock
from django.conf import settings


from ..utils.http_utils import (
    retrieve_song,
    retrieve_lyrics,
    summarize_song,
    list_countries_in_song,
)
from .mocked_data import (
    song,
    lyrics,
    summary,
    country_list,
    track_list,
    full_lyrics,
    no_lyrics,
    no_song,
)


def test_retrieve_song():
    song_params = {
        "q_artist": "Bethel",
        "q_track": "Goodness of God",
        "apikey": settings.MUSIX_API_KEY,
    }

    mock_session = Mock()
    mock_response = Mock()
    mock_session.get.return_value = mock_response
    mock_response.json.return_value = track_list

    response = retrieve_song(mock_session, song_params)
    mock_response.json.assert_called_once()
    assert response == song


def test_retrieve_lyrics():
    track_id = 28929481
    lyrics_params = {
        "track_id": track_id,
        "apikey": settings.MUSIX_API_KEY,
    }

    mock_session = Mock()
    mock_response = Mock()
    mock_session.get.return_value = mock_response
    mock_response.json.return_value = full_lyrics

    response = retrieve_lyrics(mock_session, lyrics_params)
    mock_response.json.assert_called_once()
    assert response == lyrics


def test_summarise_song():
    mock_session = Mock()
    mock_session.create.return_value = summary

    response = summarize_song(mock_session, lyrics)
    assert response == summary.choices[0].text


def test_list_countries():
    mock_session = Mock()
    mock_session.create.return_value = country_list

    response = list_countries_in_song(mock_session, lyrics)
    assert response == country_list.choices[0].text


def test_retrieve_song_not_exist():
    song_params = {
        "q_artist": "Benjamin",
        "q_track": "Good Run",
        "apikey": settings.MUSIX_API_KEY,
    }

    mock_session = Mock()
    mock_response = Mock()
    mock_session.get.return_value = mock_response
    mock_response.json.return_value = no_song

    response = retrieve_song(mock_session, song_params)
    mock_response.json.assert_called_once()
    assert response == None


def test_no_lyrics_to_retrieve():
    track_id = 289
    lyrics_params = {
        "track_id": track_id,
        "apikey": settings.MUSIX_API_KEY,
    }

    mock_session = Mock()
    mock_response = Mock()
    mock_session.get.return_value = mock_response
    mock_response.json.return_value = no_lyrics

    response = retrieve_lyrics(mock_session, lyrics_params)
    mock_response.json.assert_called_once()
    assert response == None
