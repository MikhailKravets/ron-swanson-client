import typing

import requests


class RonSwanson:
    """Get one of Ron Swanson quotes using the API.
    There are three methods available

    - one — get single quote
    - random — get N random quotes
    - search — search quote with the term

    Args:
        base_url: the URL to the Ron Swanson API
    """

    def __init__(self, base_url: str = "https://ron-swanson-quotes.herokuapp.com"):
        self.base_url = base_url

    def one(self) -> str:
        """Get one random Ron Swanson quote

        Returns:
            str: Random quote
        """
        url = f"{self.base_url}/v2/quotes/"
        return self._get(url)

    def random(self, count: int = 1) -> typing.List[str]:
        """Get random Ron Swanson quotes

        Args:
            count: the amount of quotes returned

        Returns:
            list: List of random quotes
        """
        url = f"{self.base_url}/v2/quotes/{count}"
        return self._get(url)

    def search(self, term: str) -> typing.List[str]:
        """Search Ron Swanson quotes by term

        Args:
            term: search term

        Returns:
            list: List of found quotes
        """
        url = f"{self.base_url}/v2/quotes/search/{term}"
        return self._get(url)

    def _get(self, url: str) -> typing.Union[typing.List[str], str]:
        resp = requests.get(url, headers={'Content-Type': 'application/json'})
        return resp.json()
