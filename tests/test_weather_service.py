from backend.services.weather_service import fetch_weather
import pytest


def test_fetch_weather_returns_data():
    data = fetch_weather("Budapest")

    assert "city" in data
    assert "temperature" in data
    assert "condition" in data


@pytest.mark.parametrize("city", ["Budapest", "London", "Berlin"])
def test_fetch_weather_multiple_cities(city):
    data = fetch_weather(city)

    assert data["city"]
    assert isinstance(data["temperature"], (int, float))
