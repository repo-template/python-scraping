from abc import ABCMeta, abstractmethod

import requests
from bs4 import BeautifulSoup
from requests import Response

from hogehoge.constants.headers import HEADER


class BaseScraping(metaclass=ABCMeta):
    url: str
    soup: BeautifulSoup

    def __init__(self) -> None:
        res: Response = requests.get(self.url, headers=HEADER.BASE)
        self.soup = BeautifulSoup(res.content, "html.parser")
        self._get()

    @abstractmethod
    def _get(self) -> None:
        raise NotImplementedError
