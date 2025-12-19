from fastapi import FastAPI
import logging

from weather_monitor.backend.services.scheduler import start_scheduler
from weather_monitor.backend.db.database import Base, engine, SessionLocal
from weather_monitor.backend.models.weather import Weather
from weather_monitor.backend.services.weather_service import fetch_weather, has_recent_data
from weather_monitor.backend.schemas.weather import (WeatherOut, WeatherHistoryOut)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

app = FastAPI()

print("APP DB URL:", engine.url)

Base.metadata.create_all(bind=engine)


@app.on_event("startup")
def startup_event():
    start_scheduler()


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/weather", response_model=WeatherOut)
def get_weather(city: str):
    city = city.strip().title()

    db = SessionLocal()

    # Ha nincs friss adat, lekérjük és elmentjük
    if not has_recent_data(db, city):
        data = fetch_weather(city)
        if "error" in data:
            db.close()
            return {"error": "Ismeretlen városnév"}
        if data["condition"].startswith("mock"):
            db.close()
            return {"error": "Időjárás adat nem elérhető"}
        record = Weather(
            city=data["city"],
            temperature=data["temperature"],
            condition=data["condition"],
        )

        db.add(record)
        db.commit()

    # Mindig az UTOLSÓ mérést adjuk vissza
    latest = (
        db.query(Weather)
        .filter(Weather.city == city)
        .order_by(Weather.created_at.desc())
        .first()
    )

    db.close()
    return latest


@app.get("/weather/history", response_model=list[WeatherHistoryOut])
def weather_history(city: str):
    city = city.strip().title()
    db = SessionLocal()

    records = (
        db.query(Weather)
        .filter(Weather.city == city)
        .order_by(Weather.created_at)
        .all()
    )

    db.close()
    return records
