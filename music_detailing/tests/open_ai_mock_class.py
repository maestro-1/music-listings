from dataclasses import dataclass


@dataclass
class Text:
    text: str


@dataclass
class Summary:
    choices: list[Text]
