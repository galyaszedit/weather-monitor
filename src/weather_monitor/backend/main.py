from fastapi import FastAPI
import logging

from weather_monitor.backend.services.scheduler import start_scheduler
from weather_monitor.backend.db.database import Base, engine, SessionLocal
from weather_monitor.backend.models.weather import Weather
from weather_monitor.backend.services.weather_service import fetch_weather

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


@app.get("/weather")
def get_weather(city: str):
    db = SessionLocal()
    data = fetch_weather(city)

    record = Weather(
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
    records = db.query(Weather).all()
    db.close()

    return records
