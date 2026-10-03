import os
from pathlib import Path
import streamlit as st
from mapa import MISTNOSTI

# Nastavení stránky
st.set_page_config(
    page_title="Vražda v Kuželce",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Kompaktní CSS pro zobrazení na jednu obrazovku bez nutnosti scrollování
st.markdown(
    """
    <style>
        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 0.5rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
            max-width: 1400px;
        }
        .stImage img {
            max-height: 65vh !important;
            width: 100% !important;
            object-fit: cover;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.25);
        }
        .stButton button {
            margin-bottom: 0.3rem;
            font-weight: 500;
        }
        h1, h2, h3, p {
            margin-bottom: 0.3rem !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

BASE_DIR = Path(__file__).resolve().parent

def ziskej_cestu_obrazku(nazev_souboru: str) -> str | None:
    """Vrátí platnou cestu k obrázku."""
    if not nazev_souboru:
        return None
    cesta = BASE_DIR / nazev_souboru
    if cesta.exists():
        return str(cesta)
    cesta_obrazky = BASE_DIR / "obrazky" / Path(nazev_souboru).name
    if cesta_obrazky.exists():
        return str(cesta_obrazky)
    return str(nazev_souboru)

# Inicializace stavů hry
if "aktualni_misto" not in st.session_state or st.session_state.aktualni_misto not in MISTNOSTI:
    st.session_state.aktualni_misto = "vchod"

if "detail_stolu" not in st.session_state:
    st.session_state.detail_stolu = None

misto_info = MISTNOSTI[st.session_state.aktualni_misto]
stoly_v_mistnosti = misto_info.get("stoly", {})

# Horní lišta
st.markdown("### 🍺 Vražda v Kuželce – Detektivní adventura")

# 2 sloupce: vlevo obrázek, vpravo popis a akce
col_levy, col_pravy = st.columns([1.3, 1.0], gap="large")

# 1. POHLED NA DETAIL STOLU / OBJEKTU
if st.session_state.detail_stolu is not None and st.session_state.detail_stolu in stoly_v_mistnosti:
    st_klic = st.session_state.detail_stolu
    st_info = stoly_v_mistnosti[st_klic]
    
    with col_levy:
        obr_klic = st_info.get("obrazek") or st_info.get("obrazky")
        cesta_k_obr = ziskej_cestu_obrazku(obr_klic)
        if cesta_k_obr and os.path.exists(cesta_k_obr):
            st.image(cesta_k_obr, use_container_width=True)
        else:
            st.warning(f"Obrázek `{obr_klic}` nebyl nalezen.")
            
    with col_pravy:
        st.subheader(f"🔍 {st_info.get('nazev', 'Detail')}")
        st.info(st_info.get("popis", ""))
        st.write("")
        if st.button("⬅️ Zpět do místnosti", use_container_width=True, type="primary"):
            st.session_state.detail_stolu = None
            st.rerun()

# 2. STANDARDNÍ POHLED NA MÍSTNOST
else:
    with col_levy:
        obr_klic = misto_info.get("obrazek") or misto_info.get("obrazky")
        cesta_k_obr = ziskej_cestu_obrazku(obr_klic)
        if cesta_k_obr and os.path.exists(cesta_k_obr):
            st.image(cesta_k_obr, use_container_width=True)
        else:
            st.warning(f"Obrázek `{obr_klic}` nebyl nalezen.")

    with col_pravy:
        st.subheader(f"📍 {misto_info.get('nazev', 'Neznámé místo')}")
        st.info(misto_info.get("popis", ""))

        if stoly_v_mistnosti:
            st.markdown("#### 🪑 Prozkoumat:")
            for stul_klic, stul_data in stoly_v_mistnosti.items():
                nazev_stolu = stul_data.get("nazev", stul_klic)
                if st.button(f"🔍 {nazev_stolu}", use_container_width=True, key=f"btn_stul_{stul_klic}"):
                    st.session_state.detail_stolu = stul_klic
                    st.rerun()
            st.write("")

        st.markdown("#### 🚪 Kam jít dál:")
        sousedni_mista = misto_info.get("sousedni", [])
        
        if sousedni_mista:
            for soused_klic in sousedni_mista:
                if soused_klic in MISTNOSTI:
                    soused_nazev = MISTNOSTI[soused_klic].get("nazev", soused_klic)
                    if st.button(f"➡️ {soused_nazev}", use_container_width=True, key=f"btn_nav_{soused_klic}"):
                        st.session_state.aktualni_misto = soused_klic
                        st.session_state.detail_stolu = None
                        st.rerun()
        else:
            st.success("🎉 Dosáhl jsi konce příběhu / zatčení!")

