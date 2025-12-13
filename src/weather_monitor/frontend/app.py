import streamlit as st
import pandas as pd

from weather_monitor.backend.services.weather_service import fetch_weather
from weather_monitor.backend.db.database import SessionLocal
from weather_monitor.backend.models.weather import Weather

st.set_page_config(page_title="Weather Monitor", layout="centered")

st.title("🌦️ Weather Monitor")
st.write("Egyszerű időjárásfigyelő – service layer közvetlen használatával")

city = st.text_input("Város neve", value="Budapest")

if st.button("Lekérdez"):
    try:
        data = fetch_weather(city)

        st.subheader(f"Időjárás: {data['city']}")
        st.metric("🌡️ Hőmérséklet (°C)", data["temperature"])
        st.write("Állapot:", data["condition"])
    except Exception as e:
        st.error(f"Hiba történt: {e}")

st.divider()
st.subheader("📊 Korábbi mérések")

db = SessionLocal()
history = db.query(Weather).order_by(Weather.created_at).all()
db.close()

if history:
    df = pd.DataFrame(
        [
            {
                "created_at": w.created_at,
                "temperature": w.temperature,
            }
            for w in history
        ]
    )
    df["created_at"] = pd.to_datetime(df["created_at"])
    st.line_chart(df.set_index("created_at")["temperature"])
else:
    st.info("Még nincs mentett adat")
