from fastapi import FastAPI
from backend.services.scheduler import start_scheduler
from weather_monitor.backend.db.database import Base
from weather_monitor.backend.models.weather import Weather

from backend.services.weather_service import fetch_weather
from backend.db.database import SessionLocal

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

app = FastAPI()

Base.metadata.create_all(bind=engine)

start_scheduler()

@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/weather")
def get_weather(city: str):
    db = SessionLocal()
    data = fetch_weather(city)

    record = weather.Weather(
        city=data["city"],
        temperature=data["temperature"],
        condition=data["condition"],
    )

    db.add(record)
    db.commit()
    db.refresh(record)
    db.close()

    return data


@app.get("/weather/history")
def weather_history():
    db = SessionLocal()
    records = db.query(weather.Weather).all()
    db.close()

    return records
