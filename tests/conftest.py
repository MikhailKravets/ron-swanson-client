import pytest
import requests

from unittest.mock import Mock

from ron_swanson.api import RonSwanson


@pytest.fixture(scope="module")
def quote():
    return "test quote"


@pytest.fixture(scope="function")
def mock_requests(monkeypatch, quote):
    p = Mock()
    p.return_value.json.return_value = [quote]
    monkeypatch.setattr(requests, "get", p)
    yield p


@pytest.fixture(scope="function")
def mock_requests_single_quote(monkeypatch, quote):
    p = Mock()
    p.return_value.json.return_value = quote
    monkeypatch.setattr(requests, "get", p)
    yield p


@pytest.fixture(scope="function")
def ron_swanson():
    return RonSwanson(base_url="http://example.com")
