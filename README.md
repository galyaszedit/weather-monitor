# Weather Monitor – Python Microservice Project

Ez a projekt egy mikroszerviz-szerű Python alkalmazás, amely egy időjárás-monitorozó rendszert valósít meg.
A cél a modern Python fejlesztési technológiák és paradigmák gyakorlati bemutatása.

Architektúra

A rendszer az alábbi komponensekből áll:

- **Backend**: FastAPI alapú REST API
- **Frontend**: Streamlit webes felület
- **Adatbázis**: SQLite + SQLAlchemy ORM
- **Automatizáció**: Időzített háttérfolyamat (scheduler, threading)
- **Külső API**: OpenWeatherMap API
- **Tesztelés**: pytest

---

Használt paradigmák

- **Procedurális**: vezérlési logika, szkriptek
- **Funkcionális**: tiszta függvények (pl. fetch_weather)
- **Objektumorientált**: SQLAlchemy modellek


Telepítés és futtatás:
Virtuális környezet létrehozása:
python3 -m venv venv
source venv/bin/activate

Függőségek telepítése:
pip install -r requirements.txt

Környezeti változók beállítása:
OPENWEATHER_API_KEY=IDE_JÖN_A_SAJÁT_KULCSOD

Backend indítása (FastAPI):
uvicorn backend.main:app --reload
Backend elérhető: http://127.0.0.1:8000

Frontend indítása (Streamlit):
streamlit run frontend/app.py

Automatizáció:

A backend indításakor egy háttérfolyamat automatikusan frissíti az időjárási adatokat, és elmenti azokat az adatbázisba.

Tesztelés:

Egységtesztek futtatása: pytest
A projekt parametrizált tesztet is tartalmaz @pytest.mark.parametrize használatával.

Vizualizáció:

A Streamlit felület diagramokon és statisztikákon keresztül jeleníti meg a mentett időjárási adatokat.

Deploy:

- **Backend (FastAPI)**: Render  
  https://weather-monitor-backend-87u3.onrender.com

- **Frontend (Streamlit)**: Streamlit Cloud  
  https://weather-monitor-faa9yxzb4fn4g6pnmcdj8t.streamlit.app/
