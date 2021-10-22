from hogehoge.models import Hoge, Profile
from hogehoge.scraping.profile_scraping import ProfileScraping


def get_hoge_info(hoge: Hoge) -> Profile:
    return ProfileScraping(hoge).profile  # type: ignore
