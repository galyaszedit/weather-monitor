import streamlit as st
import requests
import pandas as pd

BACKEND_URL = "https://weather-monitor-backend-87u3.onrender.com"

st.set_page_config(page_title="Időjárás monitor", layout="centered")
st.title("🌦️ Időjárás monitor")

# ─────────────────────────────────────────────
# INPUT
# ─────────────────────────────────────────────
city = st.text_input(
    "Város neve",
    placeholder="Írj be egy városnevet (pl. Budapest)",
)

city = city.strip().title()

if not city:
    st.info("👆 Kezdj el gépelni egy városnevet")
    st.stop()

# ─────────────────────────────────────────────
# AKTUÁLIS IDŐJÁRÁS
# ─────────────────────────────────────────────
try:
    response = requests.get(
        f"{BACKEND_URL}/weather",
        params={"city": city},
        timeout=5,
    )
    weather = response.json()
except Exception:
    st.error("Nem érem el a backendet 😢")
    st.stop()

if "error" in weather:
    st.error("Ilyen várost nem ismerek. Ne szórakozz velem 😄")
    st.stop()

st.subheader(f"📍 {weather['city']} – aktuális időjárás")

col1, col2 = st.columns(2)
col1.metric("🌡️ Hőmérséklet (°C)", weather["temperature"])
col2.write(f"☁️ {weather['condition']}")

st.divider()

# ─────────────────────────────────────────────
# TÖRTÉNETI ADATOK + GRAFIKON
# ─────────────────────────────────────────────
try:
    history = requests.get(
        f"{BACKEND_URL}/weather/history",
        params={"city": city},
        timeout=5,
    ).json()
except Exception:
    history = []

if history:
    df = pd.DataFrame(history)
    df["created_at"] = pd.to_datetime(df["created_at"])

    st.subheader("📈 Hőmérséklet alakulása (mentett adatok)")
    st.line_chart(
        df.set_index("created_at")["temperature"]
    )
else:
    st.info("Még nincs elég adat a grafikonhoz. Idővel megjelenik.")
