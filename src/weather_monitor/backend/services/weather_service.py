import os
import requests
import logging

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # prod környezetben nem kell

logger = logging.getLogger(__name__)

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")


def fetch_weather(city: str) -> dict:
    if not OPENWEATHER_API_KEY:
        logger.warning("API key missing, using fallback")
        return _fallback_weather(city)

    try:
        params = {
            "q": city,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric",
            "lang": "hu",
        }

        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status()

        data = response.json()

        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"],
        }

    except requests.exceptions.HTTPError as e:
        logger.error(f"Weather API error: {e}")
        return _fallback_weather(city)

    except Exception:
        logger.exception("Unexpected error")
        return _fallback_weather(city)


def _fallback_weather(city: str) -> dict:
    return {
        "city": city,
        "temperature": 22,
        "condition": "mock adat (API key nem elérhető)",
    }
