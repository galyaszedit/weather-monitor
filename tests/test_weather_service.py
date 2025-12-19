from weather_monitor.backend.services.weather_service import fetch_weather
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

def test_fetch_weather_city_name_matches():
    data = fetch_weather("Budapest")

    assert data["city"].lower() == "budapest"


def test_fetch_weather_temperature_is_reasonable():
    data = fetch_weather("Budapest")

    assert -50 < data["temperature"] < 60
