"""Tuteur IA pour Accompagner les etudiants en informatique et en  mathematique
===
App.py l'application principale
Frontend (Streamlit)
      │
      ▼
Backend (FastAPI)
      │
      ├── Pipeline RAG ──► FAISS (index vectoriel)
      │       │
      │       └── Extraction PDF → Chunks → Embeddings → Recherche contextuelle
      │
      └── Base de données (PostgreSQL)
"""

import streamlit as st 
import logging

#Configuration de la page
st.set_page_config(
    page_title = "AI Tutor",
    page_icon = "",
    layout ="wide",
    initial_sidebar_state ="expanded",
    menu_items = {
        "Get help":     "mailto:tengacherif@gmail.com",
        "Report a bug": "mailto:tengacherif@gmail.com",
        "About" : "AI Tutor V1 - L'Ia au service de l'education"
    }
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s – %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger(__name__)

def _init_session() -> None:
    "Initialise les session streamlit"
    defaults = {
        "historique" : [],
        "chat_messages" : [],
        "current_page" :"Accueil"
       
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val

#Navigation
def _render_sidebar() -> str:
    """Affiche la barre laterale"""
    with st.sidebar:
        st.markdown(f"""
        <div style="text-align:center; padding:1rem 0 .5rem;">
            <div style="font-size:3rem;"></div>
            <h2 style="color:#fff; margin:0; font-size:1.3rem; font-weight:700;">
                
            </h2>
            <p style="color:rgba(255,255,255,.6); font-size:.8rem; margin:.2rem 0 0;">
                v
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<hr style='border-color:rgba(255,255,255,.2);'>", unsafe_allow_html=True)
        
        pages =["Acceuil","Nouveau Message","Messages"]
        page = st.radio(
            "Navigation",
            pages,
            label_visibility="collapsed"
        )
        st.caption("AI Tutor 2026")
        
_PAGE_SUBTITLES = {
    "Acceuil" : "PAge d'acceuil ",
    "Nouveau message" : "Démarrer une nouvelle discution",
    "messages" : "Voir la liste des messages"
}
       
def _render_header(page: str) -> None:
    """Affiche le header de la page courante"""
    subtitle = _PAGE_SUBTITLES.get(page, "")
    st.markdown(f"""
    <div class="tuto-header">
        <h1> </h1>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)
    
def main() -> None:
    """Fonction principale – charge le modèle et route vers la bonne page."""
    # CSS global
   

    # Session
    _init_session()

    # Modèle ML

    # Sidebar + navigation
    page = _render_sidebar()

    # Header
    _render_header(page)

    # Routing


if __name__ == "__main__":
    main()
