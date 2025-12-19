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

A projekt Streamlit Cloud környezetben került deployolásra.

A Streamlit frontend a FastAPI backend REST végpontjait HTTP kéréseken keresztül hívja meg.
A backend önálló szolgáltatásként futtatható (uvicorn segítségével), a frontend és backend
rétegek logikailag elkülönülnek.

A mikroszerviz-szemléletű, rétegezett architektúra (api / services / models)
a lokális és a cloud környezetben is változatlan marad.

Megjegyzés:

Az ingyenes cloud környezetek bizonyos korlátozásai miatt a deploy során
egyes komponensek futtatási módja eltérhet a lokális fejlesztéstől,
azonban az alkalmazás architektúrája és rétegezése változatlan marad.