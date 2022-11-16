import typing

import requests


class RonSwanson:

    def __init__(self, base_url: str = "https://ron-swanson-quotes.herokuapp.com"):
        self.base_url = base_url

    def one(self) -> str:
        url = f"{self.base_url}/v2/quotes/"
        return self._get(url)

    def random(self, count: int = 1) -> typing.List[str]:
        url = f"{self.base_url}/v2/quotes/{count}"
        return self._get(url)

    def search(self, term: str) -> typing.List[str]:
        url = f"{self.base_url}/v2/quotes/search/{term}"
        return self._get(url)

    def _get(self, url: str) -> typing.Union[typing.List[str], str]:
        resp = requests.get(url, headers={'Content-Type': 'application/json'})
        return resp.json()
