# AI Tutor – Tuteur Académique Intelligent

Un assistant pédagogique basé sur l'intelligence artificielle, conçu pour aider les étudiants universitaires (mathématiques, physique, informatique, IA) dans leur apprentissage de manière personnalisée et interactive.

---

## Fonctionnalités

- **Chat intelligent** – Réponses en langage naturel, contextualisées selon les cours
- **Gestion des cours** – Upload de PDF et indexation automatique
- **Module pédagogique** – Explications progressives adaptées au niveau (L1/L2/L3)
- **Gestion utilisateur** – Authentification et historique des conversations

---

## Architecture

```
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
```

### Stack technique

| Composant       | Technologie                          |
|----------------|--------------------------------------|
| Frontend        | Streamlit                            |
| Backend         | FastAPI                              |
| IA / LLM        | LLM externe via API                  |
| RAG             | LangChain + sentence-transformers    |
| Index vectoriel | FAISS (CPU)                          |
| Base de données | PostgreSQL + SQLAlchemy              |
| Langage         | Python 3.10+                         |

---

## Structure du projet

```
ai_tutor/
├── backend/
│   ├── api/          # Endpoints FastAPI
│   ├── core/         # Configuration et utilitaires
│   ├── db/           # Modèles et sessions base de données
│   ├── models/       # Schémas Pydantic
│   ├── rag/          # Pipeline RAG (extraction, embeddings, FAISS)
│   └── services/     # Logique métier
├── frontend/         # Interface Streamlit
├── data/             # Fichiers PDF et données
├── tests/            # Tests unitaires et d'intégration
├── docs/             # Documentation technique
├── prompts/          # Templates de prompts
├── requirements.txt
└── README.md
```

---

## Installation

### Prérequis

- Python 3.10+
- PostgreSQL

### Étapes

```bash
# Cloner le projet
git clone <repo-url>
cd ai_tutor

# Créer et activer l'environnement virtuel
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/macOS

# Installer les dépendances
pip install -r requirements.txt
```

---

## Lancement

```bash
# Démarrer le backend
uvicorn backend.api.main:app --reload

# Démarrer le frontend (dans un autre terminal)
streamlit run frontend/app.py
```

---

## Pipeline RAG

1. **Extraction** – Lecture et parsing des fichiers PDF
2. **Découpage** – Segmentation en chunks pertinents
3. **Embeddings** – Génération via `sentence-transformers`
4. **Indexation** – Stockage dans FAISS
5. **Recherche** – Récupération des chunks les plus proches
6. **Génération** – Réponse produite par le LLM avec contexte injecté

---

## Critères de réussite

- Application fonctionnelle de bout en bout
- Réponses pertinentes et pédagogiques
- Architecture claire et modulaire
- Code documenté

---

## Évolutions prévues

- Génération de QCM automatiques
- Mode hors-ligne partiel
- Statistiques d'apprentissage avancées
- Version mobile
