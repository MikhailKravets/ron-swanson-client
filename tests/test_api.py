
def test_one(quote, mock_requests_single_quote, ron_swanson):
    resp = ron_swanson.one()
    assert isinstance(resp, str)
    assert resp == quote


def test_random(quote, mock_requests, ron_swanson):
    count = 1
    resp = ron_swanson.random(count=count)
    assert len(resp) == count
    assert resp[0] == quote


def test_search(quote, mock_requests, ron_swanson):
    count = 1
    resp = ron_swanson.search(term="test")
    assert len(resp) == count
    assert resp[0] == quote
