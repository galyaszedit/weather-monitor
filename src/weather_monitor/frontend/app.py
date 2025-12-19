import streamlit as st
import requests
import pandas as pd

BACKEND_URL = "http://localhost:8000"

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
    st.error("Nem érem el a backendet 😢 Fut a FastAPI?")
    st.stop()

# ⛔ ERROR ELLENŐRZÉS AZONNAL
if "error" in weather:
    st.error("Ilyen várost nem ismerek. Ne szórakozz velem 😄")
    st.stop()

# ─────────────────────────────────────────────
# MEGJELENÍTÉS – AKTUÁLIS
# ─────────────────────────────────────────────
st.subheader(f"📍 {weather['city']} – aktuális időjárás")
st.metric("🌡️ Hőmérséklet (°C)", weather["temperature"])
st.write(weather["condition"])

# ────────────────────────────────────
