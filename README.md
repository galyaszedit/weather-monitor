# Weather Monitor – Python Microservice Project

Ez a projekt egy mikroszerviz-szemléletű Python alkalmazás, amely aktuális időjárási adatokat gyűjt, tárol és jelenít meg webes felületen.

A projekt célja a modern Python szoftverfejlesztési eszközök és paradigmák gyakorlati bemutatása.

---

Funkciók:

- Időjárási adatok lekérése külső API-ból (OpenWeatherMap)
- Adatok tartós tárolása adatbázisban (SQLite)
- Automatikus, időzített adatfrissítés
- REST API FastAPI-val
- Webes felület Streamlit segítségével
- Statisztikák és vizualizációk megjelenítése
- Egységtesztek pytest használatával

---

Alkalmazott technológiák:

- **Backend:** FastAPI, SQLAlchemy, Pydantic
- **Frontend:** Streamlit
- **Adatbázis:** SQLite
- **Automatizáció:** háttérfolyamat / időzített frissítés
- **Tesztelés:** pytest
- **Külső API:** OpenWeatherMap
- **Konfiguráció:** `.env` fájl és környezeti változók


Telepítés és futtatás:
Virtuális környezet létrehozása:
python3 -m venv venv
source venv/bin/activate

Függőségek telepítése:
pip install -r requirements.txt

Környezeti változók beállítása:
Hozz létre egy .env fájlt a projekt gyökerében az alábbi minta alapján:
OPENWEATHER_API_KEY=IDE_JÖN_A_SAJÁT_KULCSOD

Backend indítása (FastAPI):
uvicorn backend.main:app --reload
Backend elérhető: http://127.0.0.1:8000
Megjegyzés:
A Streamlit alkalmazás cloud környezetben nem HTTP-n keresztül hívja a FastAPI-t,
hanem közvetlenül a backend/services réteget használja.


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

A FastAPI backend és a Streamlit frontend egy közös futtatókörnyezetben működik,
azonban a rétegezett architektúra (api / services / models) változatlanul megmaradt.

A FastAPI backend önállóan is futtatható lokálisan (backend/main.py),
azonban a Streamlit Cloud környezetben a frontend közvetlenül
a backend service layer-t használja HTTP kommunikáció nélkül,
az ingyenes cloud infrastruktúra korlátai miatt.