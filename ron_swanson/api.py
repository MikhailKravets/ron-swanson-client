import requests


class RonSwanson:

    def __init__(self, base_url: str = "https://ron-swanson-quotes.herokuapp.com"):
        self.base_url = base_url

    def random(self, count: int = 1) -> list[str]:  # typing.List[str]
        url = f"{self.base_url}/v2/quotes/{count}"
        resp = requests.get(url, headers={'Content-Type': 'application/json'})
        return resp.json()

    def search(self, term: str) -> list[str]:
        url = f"{self.base_url}/v2/quotes/search/{term}"
        resp = requests.get(url, headers={'Content-Type': 'application/json'})
        return resp.json()
