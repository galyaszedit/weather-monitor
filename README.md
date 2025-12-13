# Weather Monitor – Python Microservice Project

Ez a projekt egy mikroszerviz-szemléletű Python alkalmazás, amely aktuális időjárási adatokat gyűjt, tárol és jelenít meg webes felületen.

A projekt célja a modern Python szoftverfejlesztési eszközök és paradigmák gyakorlati bemutatása.

---

## 🎯 Funkciók

- Időjárási adatok lekérése külső API-ból (OpenWeatherMap)
- Adatok tartós tárolása adatbázisban (SQLite)
- Automatikus, időzített adatfrissítés
- REST API FastAPI-val
- Webes felület Streamlit segítségével
- Statisztikák és vizualizációk megjelenítése
- Egységtesztek pytest használatával

---

## 🧱 Alkalmazott technológiák

- **Backend:** FastAPI, SQLAlchemy, Pydantic
- **Frontend:** Streamlit
- **Adatbázis:** SQLite
- **Automatizáció:** háttérfolyamat / időzített frissítés
- **Tesztelés:** pytest
- **Külső API:** OpenWeatherMap
- **Konfiguráció:** `.env` fájl és környezeti változók

---

## 📁 Projektstruktúra

weather-monitor/
├── backend/
│   ├──__pycache__
│   ├── api/
│   ├── config
│   ├── core
│   ├── db/
│   ├── models/
│   ├── services/  
│   ├── __init__
│   └── main.py
├── frontend/
│   └── app.py
├── tests/
│   ├── conftest.py
│   ├── test_database.py
│   └── test_weather_service.py
├── .env
├── .env.example
├── README.md
├── requirements.txt
└── weather.db

⚙️ Telepítés és futtatás
1️⃣ Virtuális környezet létrehozása
python3 -m venv venv
source venv/bin/activate

2️⃣ Függőségek telepítése
pip install -r requirements.txt

3️⃣ Környezeti változók beállítása
Hozz létre egy .env fájlt a projekt gyökerében az alábbi minta alapján:
OPENWEATHER_API_KEY=IDE_JÖN_A_SAJÁT_KULCSOD

🚀 Backend indítása (FastAPI)
uvicorn backend.main:app --reload
Backend elérhető: http://127.0.0.1:8000

🌐 Frontend indítása (Streamlit)
streamlit run frontend/app.py

🤖 Automatizáció

A backend indításakor egy háttérfolyamat automatikusan frissíti az időjárási adatokat, és elmenti azokat az adatbázisba.

🧪 Tesztelés

Egységtesztek futtatása: pytest
A projekt parametrizált tesztet is tartalmaz @pytest.mark.parametrize használatával.

📊 Vizualizáció

A Streamlit felület diagramokon és statisztikákon keresztül jeleníti meg a mentett időjárási adatokat.

☁️ Deploy

Backend: Render.com
Frontend: Streamlit Cloud

(A deploy linkek a beadáskor kerülnek megadásra.)