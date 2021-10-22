from bs4 import BeautifulSoup

from hogehoge.models import Hoge, Profile
from hogehoge.scraping.base import BaseScraping


class TagClass:
    UL_CLASS = "list-area"


class ProfileScraping(BaseScraping):
    soup: BeautifulSoup
    profile: Profile

    def __init__(self, hoge: Hoge) -> None:
        self.url = hoge.url
        super().__init__()

    def _get(self) -> None:
        ul = self.soup.find("ul", class_=TagClass.UL_CLASS)

        if not ul:
            raise Exception(self.url)

        self.profile = Profile("hoge", "26", "https://image.com/aaa")
