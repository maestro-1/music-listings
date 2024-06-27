from unittest.mock import Mock
from .mocked_data import no_song, full_lyrics, track_list, no_lyrics, song_without_lyrics


def request_song():
    response_mock = Mock()
    response_mock.status_code = 200
    response_mock.json.return_value = track_list
    # the function return an instance of class Mock
    return response_mock


def request_lyrics():
    response_mock = Mock()
    response_mock.status_code = 200
    response_mock.json.return_value = full_lyrics
    # the function return an instance of class Mock
    return response_mock


def request_non_existent_song():
    response_mock = Mock()
    response_mock.status_code = 200
    response_mock.json.return_value = no_song
    # the function return an instance of class Mock
    return response_mock


def request_no_lyrics():
    response_mock = Mock()
    response_mock.status_code = 404
    response_mock.json.return_value = no_lyrics
    # the function return an instance of class Mock
    return response_mock


def request_song_without_lyrics():
    response_mock = Mock()
    response_mock.status_code = 200
    response_mock.json.return_value = song_without_lyrics
    # the function return an instance of class Mock
    return response_mock
