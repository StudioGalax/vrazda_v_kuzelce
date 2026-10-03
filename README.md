# 🍺 Vražda v Kuželce – Detektivní adventura

Interaktivní detektivní textově-vizuální adventura vytvořená v prostředí **Streamlit**.

## 📖 O hře
Hráč se ocitá v hospodě Kuželka, kde vyšetřuje záhadný zločin. Prochází jednotlivé místnosti, prozkoumává stoly, podezřelé objekty a stopy a postupně odhaluje indicie vedoucí k dopadení pachatele.

## 🚀 Jak hru spustit lokálně

1. **Klonování repozitáře:**
   ```bash
   git clone <URL_VASEHO_REPOZITARE>
   cd vrazda_v_kuzelce
   ```

2. **Instalace závislostí:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Spuštění hry:**
   ```bash
   streamlit run vrazda_hra.py
   ```

## 📁 Struktura projektu

- `vrazda_hra.py` – Hlavní herní logika a uživatelské rozhraní (Streamlit).
- `mapa.py` – Databáze lokací, místností, sousedních propojení a detailů stolů.
- `obrazky/` – Grafické podklady k jednotlivým scénám a detailům.
- `requirements.txt` – Požadované Python knihovny.
