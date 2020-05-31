from main import get_temperature
import pytest
import requests


class MockResponse:

    
    def __init__(self, expected):
		self.__expected = expected
    
    # mock json() method always returns a specific testing dictionary
    def json(self):
        return {"currently": {"temperature": self.__expected}}

@pytest.mark.parametrize("lat , lng, temperature, expected", [(-14.235004, -51.92528, 62, 16)])
def test_get_temperature(monkeypatch, lat, lng, temperature, expected):

    # Any arguments may be passed and mock_get() will always return our
    # mocked object, which only has the .json() method.
    def mock_get(*args):
        return MockResponse(temperature)

    # apply the monkeypatch for requests.get to mock_get
    monkeypatch.setattr(requests, "get", mock_get)

    result = get_temperature(lat, lng)
    # app.get_json, which contains requests.get, uses the monkeypatch
    assert result == expected


