import streamlit as st
import pandas as pd
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT_DIR))

from weather_monitor.backend.services.weather_service import fetch_weather
from weather_monitor.backend.db.database import SessionLocal
from weather_monitor.backend.models.weather import Weather

st.set_page_config(page_title="Weather Monitor", layout="centered")

st.title("Weather Monitor")


if "active_city" not in st.session_state:
    st.session_state.active_city = "Budapest"

city_input = st.text_input(
    "Város neve",
    value=st.session_state.active_city
)

if st.button("Lekérdez"):
    try:
        data = fetch_weather(city_input)
        st.session_state.active_city = data["city"]

        st.subheader(f"Aktuális időjárás – {data['city']}")
        st.metric("Hőmérséklet (°C)", data["temperature"])
        st.write("Állapot:", data["condition"])

    except Exception as e:
        st.error(f"Hiba történt: {e}")

st.divider()

db = SessionLocal()

active_city = st.session_state.active_city

st.subheader(f"Korábbi mérések – {active_city}")

history = (
    db.query(Weather)
    .filter(Weather.city == active_city)
    .order_by(Weather.created_at)
    .all()
)

if history:
    df = pd.DataFrame(
        [{
            "időpont": w.created_at,
            "hőmérséklet": w.temperature
        } for w in history]
    )

    df["időpont"] = pd.to_datetime(df["időpont"])

    st.line_chart(
        df.set_index("időpont")["hőmérséklet"]
    )
else:
    st.info("Ehhez a városhoz még nincs adat.")

db.close()
