import time
import threading
import logging

from weather_monitor.backend.services.weather_service import fetch_weather
from weather_monitor.backend.db.database import SessionLocal
from weather_monitor.backend.models.weather import Weather

logger = logging.getLogger(__name__)

CITIES = ["Budapest"]
INTERVAL_SECONDS = 3600  # 1 óra


def weather_job():
    while True:
        logger.info("Automatikus időjárás-frissítés indul")

        for city in CITIES:
            try:
                data = fetch_weather(city)

                db = SessionLocal()
                record = Weather(
                    city=data["city"],
                    temperature=data["temperature"],
                    condition=data["condition"],
                )
                db.add(record)
                db.commit()
                db.close()

                logger.info(f"Sikeres mentés: {city}")

            except Exception:
                logger.exception(f"Hiba a(z) {city} frissítésekor")

        time.sleep(INTERVAL_SECONDS)


def start_scheduler():
    thread = threading.Thread(target=weather_job, daemon=True)
    thread.start()
