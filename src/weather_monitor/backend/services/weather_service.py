import os
import requests
import logging
from datetime import datetime, timedelta

from weather_monitor.backend.models.weather import Weather

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

    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "hu",
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)

        if response.status_code == 404:
            return {"error": "CITY_NOT_FOUND"}

        response.raise_for_status()
        data = response.json()

        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"],
        }

    except requests.exceptions.HTTPError as e:
        logger.error(f"Weather API HTTP error: {e}")
        return _fallback_weather(city)

    except Exception as e:
        logger.exception("Unexpected error during weather fetch")
        return _fallback_weather(city)



def has_recent_data(db, city: str, hours: int = 1) -> bool:
    """
    Megnézi, van-e az adott városra friss (pl. 1 órán belüli) adat az adatbázisban
    """
    latest = (
        db.query(Weather)
        .filter(Weather.city == city)
        .order_by(Weather.created_at.desc())
        .first()
    )

    if not latest:
        return False

    return latest.created_at > datetime.utcnow() - timedelta(hours=hours)


def _fallback_weather(city: str) -> dict:
    """
    Mock adat, ha nincs API key vagy hiba van
    """
    return {
        "city": city,
        "temperature": 22,
        "condition": "mock adat (API key nem elérhető)",
    }
