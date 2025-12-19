from pydantic import BaseModel
from datetime import datetime


class WeatherBase(BaseModel):
    city: str
    temperature: float
    condition: str


class WeatherOut(WeatherBase):
    created_at: datetime

    class Config:
        orm_mode = True


class WeatherHistoryOut(WeatherBase):
    created_at: datetime

    class Config:
        orm_mode = True
