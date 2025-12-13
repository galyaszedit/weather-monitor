from weather_monitor.backend.db.database import SessionLocal
from weather_monitor.backend.models.weather import Weather


def test_database_insert():
    db = SessionLocal()

    print("TEST DB URL:", db.bind.url)

    record = Weather(
        city="TestCity",
        temperature=10,
        condition="teszt"
    )

    db.add(record)
    db.commit()

    result = db.query(Weather).filter_by(city="TestCity").first()
    assert result is not None

    db.delete(result)
    db.commit()
    db.close()

