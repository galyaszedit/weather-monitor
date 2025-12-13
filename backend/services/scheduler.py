import time
import threading
import logging

from backend.services.weather_service import fetch_weather
from backend.db.database import SessionLocal
from backend.models.weather import Weather

logger = logging.getLogger(__name__)

DEFAULT_CITY = "Budapest"
INTERVAL_SECONDS = 3600  # 1 óra


def weather_job():
    while True:
        try:
            logger.info("Automatikus időjárás-frissítés indul")

            data = fetch_weather(DEFAULT_CITY)

            db = SessionLocal()
            record = Weather(
                city=data["city"],
                temperature=data["temperature"],
                condition=data["condition"],
            )
            db.add(record)
            db.commit()
            db.close()

            logger.info("Időjárás mentve az adatbázisba")

        except Exception as e:
            logger.exception("Hiba az automatikus frissítés során")

        time.sleep(INTERVAL_SECONDS)


def start_scheduler():
    thread = threading.Thread(target=weather_job, daemon=True)
    thread.start()

