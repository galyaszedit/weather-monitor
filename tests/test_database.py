from backend.db.database import SessionLocal
from backend.models.weather import Weather


def test_database_insert():
    db = SessionLocal()

    record = Weather(
        city="TestCity",
        temperature=10,
        condition="teszt"
    )

    db.add(record)
    db.commit()

    result = db.query(Weather).filter_by(city="TestCity").first()

    db.close()

    assert result is not None
