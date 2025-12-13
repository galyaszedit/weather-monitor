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

db = SessionLocal()


cities = (
    db.query(Weather.city)
    .distinct()
    .order_by(Weather.city)
    .all()
)
city_list = [c[0] for c in cities]

if not city_list:
    st.info("Még nincs mentett adat")
    db.close()
    st.stop()

selected_city = st.selectbox(
    "Válassz várost a korábbi mérésekhez",
    city_list
)

st.subheader(f"📊 Korábbi mérések – {selected_city}")

history = (
    db.query(Weather)
    .filter(Weather.city == selected_city)
    .order_by(Weather.created_at)
    .all()
)

if history:
    df_city = pd.DataFrame(
        [
            {
                "created_at": w.created_at,
                "temperature": w.temperature,
            }
            for w in history
        ]
    )
    df_city["created_at"] = pd.to_datetime(df_city["created_at"])
    st.line_chart(df_city.set_index("created_at")["temperature"])
else:
    st.info("Ehhez a városhoz még nincs adat")

st.divider()

st.subheader("📈 Hőmérséklet alakulása városonként")

history_all = (
    db.query(Weather)
    .order_by(Weather.created_at)
    .all()
)
db.close()

df_all = pd.DataFrame(
    [
        {
            "created_at": w.created_at,
            "temperature": w.temperature,
            "city": w.city,
        }
        for w in history_all
    ]
)

df_all["created_at"] = pd.to_datetime(df_all["created_at"])

st.line_chart(
    df_all.pivot(
        index="created_at",
        columns="city",
        values="temperature"
    )
)
