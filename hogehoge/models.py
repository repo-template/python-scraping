from dataclasses import dataclass


@dataclass
class Hoge:
    name: str
    url: str


@dataclass
class Profile:
    name: str
    age: str
    image_url: str
