from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from weather_monitor.backend.db.database import Base


class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    temperature = Column(Float)
    condition = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
