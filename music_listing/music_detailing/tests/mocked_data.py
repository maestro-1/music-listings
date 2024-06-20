from dataclasses import dataclass

from .open_ai_mock_class import Summary, Text


song = {
    "track_id": 232321,
    "track_name": "Goodness of God",
    "track_name_translation_list": [],
    "track_rating": 90,
    "commontrack_id": 1232,
    "instrumental": 0,
    "explicit": 0,
    "has_lyrics": 1,
    "has_subtitles": 1,
    "has_richsync": 1,
    "num_favourite": 265,
    "album_id": 35774004,
    "album_name": "Without Words: Genesis",
    "artist_id": 123212,
    "artist_name": "Bethel Music",
    "track_share_url": "https://www.musixmatch.com/lyrics/Bethel-Music-3/Goodness-of-God",
    "track_edit_url": "https://www.musixmatch.com/lyrics/Bethel-Music-3/Goodness-of-God/",
    "restricted": 0,
    "updated_time": "2022-07-09T09:48:59Z",
    "primary_genres": {
        "music_genre_list": [
            {
                "music_genre": {
                    "music_genre_id": 1038,
                    "music_genre_parent_id": 6,
                    "music_genre_name": "Country Gospel",
                    "music_genre_name_extended": "Country / Country Gospel",
                    "music_genre_vanity": "Country-Country-Gospel",
                }
            },
            {
                "music_genre": {
                    "music_genre_id": 1103,
                    "music_genre_parent_id": 22,
                    "music_genre_name": "Praise & Worship",
                    "music_genre_name_extended": "Christian & Gospel / Praise & Worship",
                    "music_genre_vanity": "Christian-Gospel-Praise-Worship",
                }
            },
            {
                "music_genre": {
                    "music_genre_id": 22,
                    "music_genre_parent_id": 34,
                    "music_genre_name": "Christian & Gospel",
                    "music_genre_name_extended": "Christian & Gospel",
                    "music_genre_vanity": "Christian-Gospel",
                }
            },
        ]
    },
}

track_list = {
    "message": {
        "header": {
            "status_code": 200,
            "execute_time": 0.10100483894348,
            "available": 28,
        },
        "body": {
            "track_list": [
                {
                    "track": {
                        "track_id": 232321,
                        "track_name": "Goodness of God",
                        "track_name_translation_list": [],
                        "track_rating": 90,
                        "commontrack_id": 1232,
                        "instrumental": 0,
                        "explicit": 0,
                        "has_lyrics": 1,
                        "has_subtitles": 1,
                        "has_richsync": 1,
                        "num_favourite": 265,
                        "album_id": 35774004,
                        "album_name": "Without Words: Genesis",
                        "artist_id": 123212,
                        "artist_name": "Bethel Music",
                        "track_share_url": "https://www.musixmatch.com/lyrics/Bethel-Music-3/Goodness-of-God",
                        "track_edit_url": "https://www.musixmatch.com/lyrics/Bethel-Music-3/Goodness-of-God/",
                        "restricted": 0,
                        "updated_time": "2022-07-09T09:48:59Z",
                        "primary_genres": {
                            "music_genre_list": [
                                {
                                    "music_genre": {
                                        "music_genre_id": 1038,
                                        "music_genre_parent_id": 6,
                                        "music_genre_name": "Country Gospel",
                                        "music_genre_name_extended": "Country / Country Gospel",
                                        "music_genre_vanity": "Country-Country-Gospel",
                                    }
                                },
                                {
                                    "music_genre": {
                                        "music_genre_id": 1103,
                                        "music_genre_parent_id": 22,
                                        "music_genre_name": "Praise & Worship",
                                        "music_genre_name_extended": "Christian & Gospel / Praise & Worship",
                                        "music_genre_vanity": "Christian-Gospel-Praise-Worship",
                                    }
                                },
                                {
                                    "music_genre": {
                                        "music_genre_id": 22,
                                        "music_genre_parent_id": 34,
                                        "music_genre_name": "Christian & Gospel",
                                        "music_genre_name_extended": "Christian & Gospel",
                                        "music_genre_vanity": "Christian-Gospel",
                                    }
                                },
                            ]
                        },
                    }
                },
                {
                    "track": {
                        "track_id": 195217201,
                        "track_name": "Goodness of God",
                        "track_name_translation_list": [],
                        "track_rating": 75,
                        "commontrack_id": 109404590,
                        "instrumental": 0,
                        "explicit": 0,
                        "has_lyrics": 1,
                        "has_subtitles": 1,
                        "has_richsync": 1,
                        "num_favourite": 232,
                        "album_id": 37558953,
                        "album_name": "Peace",
                        "artist_id": 45008938,
                        "artist_name": "Bethel Music feat. Jenn Johnson",
                        "track_share_url": "https://www.musixmatch.com/lyrics/Bethel-Music-Jenn-Johnson-1/Goodness-of-God?utm_source=application&utm_campaign=api&utm_medium=Alex%3A1409624502044",
                        "track_edit_url": "https://www.musixmatch.com/lyrics/Bethel-Music-Jenn-Johnson-1/Goodness-of-God/edit?utm_source=application&utm_campaign=api&utm_medium=Alex%3A1409624502044",
                        "restricted": 0,
                        "updated_time": "2023-03-03T09:42:36Z",
                        "primary_genres": {
                            "music_genre_list": [
                                {
                                    "music_genre": {
                                        "music_genre_id": 1103,
                                        "music_genre_parent_id": 22,
                                        "music_genre_name": "Praise & Worship",
                                        "music_genre_name_extended": "Christian & Gospel / Praise & Worship",
                                        "music_genre_vanity": "Christian-Gospel-Praise-Worship",
                                    }
                                }
                            ]
                        },
                    }
                },
                {
                    "track": {
                        "track_id": 200411034,
                        "track_name": "Goodness of God",
                        "track_name_translation_list": [],
                        "track_rating": 1,
                        "commontrack_id": 113861180,
                        "instrumental": 0,
                        "explicit": 0,
                        "has_lyrics": 0,
                        "has_subtitles": 0,
                        "has_richsync": 0,
                        "num_favourite": 0,
                        "album_id": 39293706,
                        "album_name": "Branch Worship",
                        "artist_id": 46046026,
                        "artist_name": "Branch Music",
                        "track_share_url": "https://www.musixmatch.com/lyrics/Branch-Music/Goodness-of-God?utm_source=application&utm_campaign=api&utm_medium=Alex%3A1409624502044",
                        "track_edit_url": "https://www.musixmatch.com/lyrics/Branch-Music/Goodness-of-God/edit?utm_source=application&utm_campaign=api&utm_medium=Alex%3A1409624502044",
                        "restricted": 0,
                        "updated_time": "2020-07-28T09:01:46Z",
                        "primary_genres": {
                            "music_genre_list": [
                                {
                                    "music_genre": {
                                        "music_genre_id": 22,
                                        "music_genre_parent_id": 34,
                                        "music_genre_name": "Christian & Gospel",
                                        "music_genre_name_extended": "Christian & Gospel",
                                        "music_genre_vanity": "Christian-Gospel",
                                    }
                                }
                            ]
                        },
                    }
                },
                {
                    "track": {
                        "track_id": 285489124,
                        "track_name": "Goodness of God",
                        "track_name_translation_list": [],
                        "track_rating": 1,
                        "commontrack_id": 176889012,
                        "instrumental": 0,
                        "explicit": 0,
                        "has_lyrics": 0,
                        "has_subtitles": 0,
                        "has_richsync": 0,
                        "num_favourite": 0,
                        "album_id": 64446333,
                        "album_name": "Goodness of God",
                        "artist_id": 60067472,
                        "artist_name": "Churchome Music",
                        "track_share_url": "https://www.musixmatch.com/lyrics/Churchome-Music/Goodness-of-God?utm_source=application&utm_campaign=api&utm_medium=Alex%3A1409624502044",
                        "track_edit_url": "https://www.musixmatch.com/lyrics/Churchome-Music/Goodness-of-God/edit?utm_source=application&utm_campaign=api&utm_medium=Alex%3A1409624502044",
                        "restricted": 0,
                        "updated_time": "2024-04-30T07:25:29Z",
                        "primary_genres": {
                            "music_genre_list": [
                                {
                                    "music_genre": {
                                        "music_genre_id": 1103,
                                        "music_genre_parent_id": 22,
                                        "music_genre_name": "Praise & Worship",
                                        "music_genre_name_extended": "Christian & Gospel / Praise & Worship",
                                        "music_genre_vanity": "Christian-Gospel-Praise-Worship",
                                    }
                                }
                            ]
                        },
                    }
                },
                {
                    "track": {
                        "track_id": 209665984,
                        "track_name": "Goodness of God",
                        "track_name_translation_list": [],
                        "track_rating": 1,
                        "commontrack_id": 121943685,
                        "instrumental": 0,
                        "explicit": 0,
                        "has_lyrics": 0,
                        "has_subtitles": 0,
                        "has_richsync": 0,
                        "num_favourite": 0,
                        "album_id": 42451978,
                        "album_name": "Goodness of God",
                        "artist_id": 47883285,
                        "artist_name": "STM Music",
                        "track_share_url": "https://www.musixmatch.com/lyrics/STM-Music/Goodness-of-God?utm_source=application&utm_campaign=api&utm_medium=Alex%3A1409624502044",
                        "track_edit_url": "https://www.musixmatch.com/lyrics/STM-Music/Goodness-of-God/edit?utm_source=application&utm_campaign=api&utm_medium=Alex%3A1409624502044",
                        "restricted": 0,
                        "updated_time": "2021-02-28T04:01:57Z",
                        "primary_genres": {"music_genre_list": []},
                    }
                },
                {
                    "track": {
                        "track_id": 163281864,
                        "track_name": "Goodness of God (Live)",
                        "track_name_translation_list": [],
                        "track_rating": 77,
                        "commontrack_id": 91132642,
                        "instrumental": 0,
                        "explicit": 0,
                        "has_lyrics": 1,
                        "has_subtitles": 1,
                        "has_richsync": 1,
                        "num_favourite": 193,
                        "album_id": 31036253,
                        "album_name": "Goodness of God (Live)",
                        "artist_id": 13879449,
                        "artist_name": "Bethel Music feat. Jenn Johnson",
                        "track_share_url": "https://www.musixmatch.com/lyrics/Bethel-Music-feat-Jenn-Johnson/Goodness-of-God-Live?utm_source=application&utm_campaign=api&utm_medium=Alex%3A1409624502044",
                        "track_edit_url": "https://www.musixmatch.com/lyrics/Bethel-Music-feat-Jenn-Johnson/Goodness-of-God-Live/edit?utm_source=application&utm_campaign=api&utm_medium=Alex%3A1409624502044",
                        "restricted": 0,
                        "updated_time": "2022-01-25T19:02:58Z",
                        "primary_genres": {
                            "music_genre_list": [
                                {
                                    "music_genre": {
                                        "music_genre_id": 1094,
                                        "music_genre_parent_id": 22,
                                        "music_genre_name": "CCM",
                                        "music_genre_name_extended": "Christian & Gospel / CCM",
                                        "music_genre_vanity": "Christian-Gospel-CCM",
                                    }
                                },
                                {
                                    "music_genre": {
                                        "music_genre_id": 22,
                                        "music_genre_parent_id": 34,
                                        "music_genre_name": "Christian & Gospel",
                                        "music_genre_name_extended": "Christian & Gospel",
                                        "music_genre_vanity": "Christian-Gospel",
                                    }
                                },
                            ]
                        },
                    }
                },
                {
                    "track": {
                        "track_id": 261833872,
                        "track_name": "Goodness of God (Live)",
                        "track_name_translation_list": [],
                        "track_rating": 4,
                        "commontrack_id": 163188074,
                        "instrumental": 0,
                        "explicit": 0,
                        "has_lyrics": 0,
                        "has_subtitles": 0,
                        "has_richsync": 0,
                        "num_favourite": 0,
                        "album_id": 58465015,
                        "album_name": "Live From The Cove",
                        "artist_id": 54934571,
                        "artist_name": "Oceans Music",
                        "track_share_url": "https://www.musixmatch.com/lyrics/Oceans-Music/Goodness-of-God-Live?utm_source=application&utm_campaign=api&utm_medium=Alex%3A1409624502044",
                        "track_edit_url": "https://www.musixmatch.com/lyrics/Oceans-Music/Goodness-of-God-Live/edit?utm_source=application&utm_campaign=api&utm_medium=Alex%3A1409624502044",
                        "restricted": 0,
                        "updated_time": "2023-09-26T23:44:36Z",
                        "primary_genres": {"music_genre_list": []},
                    }
                },
                {
                    "track": {
                        "track_id": 221925029,
                        "track_name": "Goodness of God (Live)",
                        "track_name_translation_list": [],
                        "track_rating": 1,
                        "commontrack_id": 132121317,
                        "instrumental": 0,
                        "explicit": 0,
                        "has_lyrics": 0,
                        "has_subtitles": 0,
                        "has_richsync": 0,
                        "num_favourite": 0,
                        "album_id": 46403681,
                        "album_name": "No More Graves (Live at Hillcrest Baptist Church)",
                        "artist_id": 50606300,
                        "artist_name": "Hillcrest Music",
                        "track_share_url": "https://www.musixmatch.com/lyrics/Hillcrest-Music/Goodness-of-God-Live?utm_source=application&utm_campaign=api&utm_medium=Alex%3A1409624502044",
                        "track_edit_url": "https://www.musixmatch.com/lyrics/Hillcrest-Music/Goodness-of-God-Live/edit?utm_source=application&utm_campaign=api&utm_medium=Alex%3A1409624502044",
                        "restricted": 0,
                        "updated_time": "2021-08-18T19:14:14Z",
                        "primary_genres": {
                            "music_genre_list": [
                                {
                                    "music_genre": {
                                        "music_genre_id": 34,
                                        "music_genre_parent_id": 0,
                                        "music_genre_name": "Music",
                                        "music_genre_name_extended": "Music",
                                        "music_genre_vanity": "Music",
                                    }
                                }
                            ]
                        },
                    }
                },
                {
                    "track": {
                        "track_id": 224137847,
                        "track_name": "The Goodness of God",
                        "track_name_translation_list": [],
                        "track_rating": 1,
                        "commontrack_id": 134057466,
                        "instrumental": 0,
                        "explicit": 0,
                        "has_lyrics": 0,
                        "has_subtitles": 0,
                        "has_richsync": 0,
                        "num_favourite": 0,
                        "album_id": 47237405,
                        "album_name": "A Call to Worship",
                        "artist_id": 47406421,
                        "artist_name": "Thinking Music",
                        "track_share_url": "https://www.musixmatch.com/lyrics/Thinking-Music/The-Goodness-of-God?utm_source=application&utm_campaign=api&utm_medium=Alex%3A1409624502044",
                        "track_edit_url": "https://www.musixmatch.com/lyrics/Thinking-Music/The-Goodness-of-God/edit?utm_source=application&utm_campaign=api&utm_medium=Alex%3A1409624502044",
                        "restricted": 0,
                        "updated_time": "2021-10-05T03:03:16Z",
                        "primary_genres": {
                            "music_genre_list": [
                                {
                                    "music_genre": {
                                        "music_genre_id": 34,
                                        "music_genre_parent_id": 0,
                                        "music_genre_name": "Music",
                                        "music_genre_name_extended": "Music",
                                        "music_genre_vanity": "Music",
                                    }
                                }
                            ]
                        },
                    }
                },
                {
                    "track": {
                        "track_id": 289503351,
                        "track_name": "Goodness of God Acoustic (Live)",
                        "track_name_translation_list": [],
                        "track_rating": 3,
                        "commontrack_id": 179354728,
                        "instrumental": 0,
                        "explicit": 0,
                        "has_lyrics": 0,
                        "has_subtitles": 0,
                        "has_richsync": 0,
                        "num_favourite": 0,
                        "album_id": 65590319,
                        "album_name": "Acoustic Sessions (Live)",
                        "artist_id": 46301276,
                        "artist_name": "Adoration Music",
                        "track_share_url": "https://www.musixmatch.com/lyrics/Adoration-Music-1/Goodness-of-God-Acoustic-Live?utm_source=application&utm_campaign=api&utm_medium=Alex%3A1409624502044",
                        "track_edit_url": "https://www.musixmatch.com/lyrics/Adoration-Music-1/Goodness-of-God-Acoustic-Live/edit?utm_source=application&utm_campaign=api&utm_medium=Alex%3A1409624502044",
                        "restricted": 0,
                        "updated_time": "2024-06-06T23:26:58Z",
                        "primary_genres": {
                            "music_genre_list": [
                                {
                                    "music_genre": {
                                        "music_genre_id": 10,
                                        "music_genre_parent_id": 34,
                                        "music_genre_name": "Singer/Songwriter",
                                        "music_genre_name_extended": "Singer/Songwriter",
                                        "music_genre_vanity": "Singer-Songwriter",
                                    }
                                }
                            ]
                        },
                    }
                },
            ]
        },
    }
}


full_lyrics = {
    "message": {
        "header": {"status_code": 200, "execute_time": 0.0080928802490234},
        "body": {
            "lyrics": {
                "lyrics_id": 28929481,
                "explicit": 0,
                "lyrics_body": "I love You, Lord\nOh, your mercy never failed me\nAll my days, I've been held in your hands\nFrom the moment that i wake up\nUntil i lay my head\nOh, i will sing of the goodness of God\n\nAnd all my life you have been faithful\nAnd all my life you have been so, so good\nWith every breath that i am able\nOh, i will sing of the goodness of God\n\nI love your voice\nYou have led me through the fire\nAnd in darkest night you are close like no other\n...\n\n******* This Lyrics is NOT for Commercial use *******\n(1409624502044)",
                "script_tracking_url": "https://tracking.musixmatch.com/t1.0/m_js/e_1/sn_0/l_28929481/su_0/rs_0/tr_3vUCACLUAc3mNPqMU8QgLppf2ok0ZN_3UBhGilIKPyf1IiJFnJyyx3u3PNiD3DXJdApoSp6nILuOU4F9Zg3f4pLCPxLSggraTo1EAe2RdLOLcMc7ta7uEFaBgIyO2RgVKaNcSMyW46g42v3qF8hJyznv1skZWYp-g-VDFqTXrT8QUudNvOtLzJ8RCISYXA6iZvU5KW1pHEA9mZAgFtxN5wwQKWdbhWWDgKcmb137lenLDRfncjjX5V63pHTaa0cO_SY180hDLCctQTUohZashbfqpRxao7KOH-mFma28QPlqYIHn-9JeBJibIQEi_4oIgvYrBHsL7YDaRXX7b7FB_nbE9I_V4QvQaXi7F9WvoaAFXbHtOXtWuVXsq39462JOBwMptjbWWj9t7j79vuMdW3fZIzBfewyFDWEd15dvXWp9siC-gtPpn4yTDIzC5yihGaWGHuNLepA/",
                "pixel_tracking_url": "https://tracking.musixmatch.com/t1.0/m_img/e_1/sn_0/l_28929481/su_0/rs_0/tr_3vUCANx-fK5fSQhSXzCWtJW9TW0QD-nhroN8KZfVLMsBYUTMsVZ9zrT9TRzuWPcnwMoucE-3c49fpP5UJegO2W6tu6drWi8Wk_ZMRgNKyi1s-346JhlAz0IquJLBa38Nrqvhn-CmeDTJQlIutWvnqTXgvRzR6F8Nco-FzILNC8W92LiT6uA3yJi_WID3mRmcvG14v2knAbY-oGRn3xrbqWpySyhBrfLCCY9XOOt0pKUXt3__5q7xx66yLgMJYeD14cYoKdzGeQBuMBvsTeTbprW9I-pNJPnBhpok0vVtQpHJPdp1wE6qLl1u47cFket8dCwUMG2QHWhPQih_cNSC4sFfbKKkSW1h4vNRz6tbNLufKjIWFG42CYK47HJWz5ndLBUDO4IXeNMpxZ7Z-GtIa21CRFVQ8xfPAkxLgYTmDhUVuRKdHkjqBWYd_GyaNehiHL3-30M0Zyg/",
                "lyrics_copyright": "Lyrics powered by www.musixmatch.com. This Lyrics is NOT for Commercial use and only 30% of the lyrics are returned.",
                "updated_time": "2024-05-07T22:29:05Z",
            }
        },
    }
}


lyrics = "I love You, Lord\nOh, your mercy never failed me\nAll my days, I've been held in your hands\nFrom the moment that i wake up\nUntil i lay my head\nOh, i will sing of the goodness of God\n\nAnd all my life you have been faithful\nAnd all my life you have been so, so good\nWith every breath that i am able\nOh, i will sing of the goodness of God\n\nI love your voice\nYou have led me through the fire\nAnd in darkest night you are close like no other\n...\n\n******* This Lyrics is NOT for Commercial use *******\n(1409624502044)"


summary = Summary(
    choices=[
        Text(
            "I will praise and sing of the goodness and faithfulness of God, who has never failed me and has been with me every day of my life, leading me through difficult times and always being near."
        )
    ]
)

country_list = Summary(choices=[Text("None.")])

no_song = {
    "message": {
        "header": {
            "status_code": 200,
            "execute_time": 0.058937072753906,
            "available": 0,
        },
        "body": {"track_list": []},
    }
}

no_lyrics = {
    "message": {
        "header": {"status_code": 404, "execute_time": 0.070285081863403},
        "body": [],
    }
}
