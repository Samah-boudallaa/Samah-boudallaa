# Samah Boudallaa

**Étudiante en Bachelor Sciences des Données | Data Engineering, Machine Learning et IA**

Étudiante à l'EST Kelâa des Sraghna (Université Cadi Ayyad), je construis des solutions de bout en bout : de la donnée brute au modèle exposé par une API, avec des tests, des conteneurs et un suivi des performances. Je m'intéresse de plus en plus au ML Engineering, à l'industrialisation et à la fiabilité des pipelines.

[Portfolio](https://samah-boudallaa.github.io) | [LinkedIn](https://www.linkedin.com/in/samah-boudallaa-92409a329) | [E-mail](mailto:samahboudallaa@gmail.com)

---

## Parcours

- **2026 - en cours** : Bachelor Sciences des Données, EST Kelâa des Sraghna (Université Cadi Ayyad)
- **2024 - 2026** : DUT Ingénierie des Données, mention Bien, EST Kelâa des Sraghna (Université Cadi Ayyad)
- **2025 - 2026** : trois stages : développement d'applications (Municipalité de Kelâa des Sraghna, été 2025), data engineering et IA (D-Business Consulting, avril à juin 2026), data et BI (Groupe A. Lazrak Immobilier, juin à août 2026)

---

## Compétences

| Domaine | Technologies |
|---|---|
| Langages | Python, SQL, R, C |
| Data engineering | Kafka, Spark, Pandas, ETL, DuckDB, Parquet, SQL Server, MySQL |
| Machine learning | Scikit-learn, XGBoost, Isolation Forest, RAG, LangChain, Mistral AI |
| API et interfaces | FastAPI, Flask, REST, Streamlit |
| Outils | Docker, Docker Compose, Git, GitHub Actions, pytest, ruff, Prometheus, Grafana |

Ces technologies viennent de mes stages et de mes projets ; leur niveau de maîtrise n'est pas identique pour toutes.

---

## Projets

### NexaDecide

*Plateforme d'aide à la décision, réalisée pendant mon stage chez D-Business Consulting (avril à juin 2026).*

- Pipeline ETL de **443 154 enregistrements** : SQL Server vers DuckDB et Parquet. Lecture du cache en **moins de 100 ms**, contre 15 à 30 s en interrogation directe de SQL Server
- API **FastAPI** de 9 endpoints et interface **Streamlit** de 10 pages
- Prévision du chiffre d'affaires avec **XGBoost** (MAPE de 8,9 %, mesuré sur des données simulées)
- Recommandations avec **Mistral AI**, **LangChain** et **RAG**
- Connexion à Odoo CRM par XML-RPC, sur une instance de test

**Stack :** Python, FastAPI, Streamlit, DuckDB, Parquet, XGBoost, LangChain, Mistral AI
**Dépôt :** [nexadecide-decision-system](https://github.com/Samah-boudallaa/nexadecide-decision-system)

### Smart Data Pipeline

*Projet de fin d'études du DUT, réalisé en équipe de trois (2026).*

- Pipeline temps réel sur un flux simulé d'environ 132 000 mesures, avec **Kafka** en mode KRaft
- Traitement adaptatif **Pandas / Spark** et détection d'anomalies avec **Isolation Forest**
- Supervision avec **Prometheus** (8 métriques) et **Grafana**, six conteneurs orchestrés avec **Docker Compose**
- Tests locaux : moins de 500 ms par message et plus de 28 400 messages traités sans perte

**Stack :** Python, Kafka, Spark, Pandas, Isolation Forest, Prometheus, Grafana, Docker Compose
**Dépôt :** [smart-data-pipeline-pfe](https://github.com/Samah-boudallaa/smart-data-pipeline-pfe)

### GraphGen

*Application web d'analyse exploratoire de fichiers CSV et Excel, réalisée en binôme avec [Chaymae El Bahloul](https://github.com/Chaymae-El-Bahloul).*

- Application **Flask** avec des graphiques interactifs **Plotly**
- **12 tests pytest**, linter **ruff** et intégration continue **GitHub Actions**
- Conteneur **Docker** non-root avec healthcheck

**Stack :** Python, Flask, Plotly, pytest, ruff, GitHub Actions, Docker
**Dépôt :** [GraphGen](https://github.com/Samah-boudallaa/GraphGen)

> Les résultats chiffrés proviennent de tests locaux ou de données simulées.

---

## En cours d'exploration

Ces sujets ne sont pas encore pratiqués en production :

- Suivi d'expériences et versioning de modèles avec **MLflow**
- Détection de dérive des données et des modèles
- CI/CD appliqué au machine learning
- **Kubernetes**, Linux et Bash

---

## Contact

[Portfolio](https://samah-boudallaa.github.io) | [LinkedIn](https://www.linkedin.com/in/samah-boudallaa-92409a329) | [samahboudallaa@gmail.com](mailto:samahboudallaa@gmail.com)

Ouverte aux stages et aux opportunités en data, machine learning et IA.
