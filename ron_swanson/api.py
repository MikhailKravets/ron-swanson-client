import requests


class RonSwanson:

    def __init__(self, base_url: str = "https://ron-swanson-quotes.herokuapp.com"):
        self.base_url = base_url

    def random(self) -> str:
        url = f"{self.base_url}/v2/quotes"
        resp = requests.get(url, headers={'Content-Type': 'application/json'})
        return resp.json()[0]
