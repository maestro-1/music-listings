from openai import OpenAI
import requests


def retrieve_song(session: requests.Session, params: dict[str, str]) -> dict[str, any]:
    res = session.get("http://api.musixmatch.com/ws/1.1/track.search", params=params)
    desired_track = res.json()["message"]["body"]["track_list"]

    if len(desired_track) > 0:
        return desired_track[0]["track"]
    return None


def retrieve_lyrics(session: requests.Session, params: dict[str, str]):
    res = session.get(
        "http://api.musixmatch.com/ws/1.1/track.lyrics.get", params=params
    )
    response_message = res.json()["message"]
    response_body = response_message["body"]
    response_header_status = response_message["header"]["status_code"]
    if response_header_status != 200:
        return None
    return response_body["lyrics"]["lyrics_body"]


def summarize_song(client: OpenAI, lyrics: str):
    prompt = f"Please summarize the following text into one sentence:\n{lyrics}\n"
    response = client.create(
        model="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=400, temperature=0.5
    )
    summary = response.choices[0].text.strip()
    return summary


def list_countries_in_song(client: OpenAI, lyrics: str):
    prompt = f"Please list all countries mentioned in the following text otherwise return 'None':\n{lyrics}\n"
    response = client.create(
        model="gpt-3.5-turbo-instruct", prompt=prompt, max_tokens=400, temperature=0.5
    )
    country_list = response.choices[0].text.strip()
    return country_list
