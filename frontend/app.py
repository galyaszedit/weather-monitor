import streamlit as st
import requests
import pandas as pd

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Weather Monitor", layout="centered")

st.title("🌦️ Weather Monitor")
st.write("Egyszerű időjárásfigyelő – backend + frontend + adatbázis")

city = st.text_input("Város neve", value="Budapest")

if st.button("Lekérdez"):
    response = requests.get(
        f"{BACKEND_URL}/weather",
        params={"city": city},
        timeout=5,
    )

    if response.status_code == 200:
        data = response.json()

        st.subheader(f"Időjárás: {data['city']}")
        st.metric("🌡️ Hőmérséklet (°C)", data["temperature"])
        st.write("Állapot:", data["condition"])
    else:
        st.error("Backend nem válaszol 😬")

st.divider()

st.subheader("📊 Korábbi mérések")

history_response = requests.get(f"{BACKEND_URL}/weather/history")

if history_response.status_code == 200:
    history = history_response.json()

    if history:
        df = pd.DataFrame(history)
        df["created_at"] = pd.to_datetime(df["created_at"])

        st.line_chart(
            df.set_index("created_at")["temperature"]
        )
    else:
        st.info("Még nincs adat")
else:
    st.error("Nem sikerült lekérni a history-t")
