# Bonjour, je suis Samah Boudallaa

**Étudiante en Bachelor Data Science (Université Cadi Ayyad) · Data Engineering & Machine Learning · Orientation MLOps / AIOps**

Je construis des pipelines de données et de machine learning de bout en bout : de la donnée brute jusqu'au modèle exposé par une API, conteneurisé, testé et supervisé. Je cherche un poste **MLOps / AIOps Engineer** pour industrialiser et fiabiliser des modèles en production.

Maroc | [Portfolio](https://samah-boudallaa.github.io) | [LinkedIn](https://www.linkedin.com/in/samahboudallaa-92409a329) | [samahboudallaa@gmail.com](mailto:samahboudallaa@gmail.com)

---

## Stack

| Domaine | Outils |
|---|---|
| Langages | Python, SQL, R |
| Data Engineering | Apache Kafka, Apache Spark, Pandas, ETL, DuckDB, Parquet, SQL Server, MySQL |
| Machine Learning | Scikit-learn, XGBoost, Isolation Forest, RAG, LangChain, Mistral AI |
| API | FastAPI, Flask, REST, Streamlit |
| Conteneurisation, CI/CD, observabilité | Docker, Docker Compose, Git, GitHub Actions, pytest, ruff, Prometheus, Grafana |

---

## Projets mis en avant

### 1. NexaDecide : plateforme d'aide à la décision basée sur l'IA
Réalisé pendant mon stage chez D-Business Consulting (2026).
- Pipeline ETL de **443 154 enregistrements** (SQL Server → DuckDB / Parquet) : lecture en **< 100 ms** contre 15 à 30 s en accès direct
- API **FastAPI** (9 endpoints, route de santé) et interface **Streamlit** de 10 pages
- Modèle **XGBoost** de prévision du chiffre d'affaires (MAPE 8,9 % sur données simulées) et recommandations **Mistral AI / LangChain (RAG)**
- Dépôt : [nexadecide-decision-system](https://github.com/Samah-boudallaa/nexadecide-decision-system)

### 2. Smart Data Pipeline : pipeline IoT temps réel (PFE DUT, équipe de 3)
- Architecture événementielle **Kafka (KRaft)** sur ~132 000 mesures de capteurs, moteur adaptatif Pandas / Spark
- Détection d'anomalies par **Isolation Forest**
- Supervision avec **Prometheus** (8 métriques) et **Grafana** ; 6 conteneurs orchestrés avec **Docker Compose**
- Tests en local : traitement < 500 ms par message, 28 400+ messages traités sans perte
- Dépôt : [smart-data-pipeline-pfe](https://github.com/Samah-boudallaa/smart-data-pipeline-pfe)

### 3. GraphGen : analyse exploratoire de fichiers CSV / Excel (binôme)
- Application web Flask / Plotly
- **12 tests pytest**, linter **ruff**, intégration continue **GitHub Actions**
- Conteneur **Docker** non-root avec healthcheck
- Dépôt : [GraphGen](https://github.com/Samah-boudallaa/GraphGen)

> Chaque dépôt contient un README avec l'architecture, la commande de lancement et les résultats.

---

## Preuves de compétences

Chaque compétence attendue pour un poste MLOps / AIOps, avec le dépôt où la vérifier.

| Attente du poste | Preuve | Où la voir |
|---|---|---|
| Conteneurisation et déploiement | Docker Compose avec 6 services ; conteneur non-root avec healthcheck | [smart-data-pipeline-pfe](https://github.com/Samah-boudallaa/smart-data-pipeline-pfe), [GraphGen](https://github.com/Samah-boudallaa/GraphGen) |
| CI/CD et tests automatisés | GitHub Actions, 12 tests pytest, linter ruff | [GraphGen](https://github.com/Samah-boudallaa/GraphGen), [onglet Actions](https://github.com/Samah-boudallaa/GraphGen/actions) |
| Monitoring et observabilité | Prometheus (8 métriques) et dashboard Grafana | [smart-data-pipeline-pfe](https://github.com/Samah-boudallaa/smart-data-pipeline-pfe) |
| Détection d'anomalies (AIOps) | Isolation Forest sur un flux Kafka temps réel | [smart-data-pipeline-pfe](https://github.com/Samah-boudallaa/smart-data-pipeline-pfe) |
| Mise à disposition de modèles ML | API FastAPI (9 endpoints) servant un modèle XGBoost | [nexadecide-decision-system](https://github.com/Samah-boudallaa/nexadecide-decision-system) |
| Pipelines de données fiables | ETL de 443 154 enregistrements, lecture < 100 ms ; 28 400+ messages traités sans perte (tests en local) | [nexadecide-decision-system](https://github.com/Samah-boudallaa/nexadecide-decision-system), [smart-data-pipeline-pfe](https://github.com/Samah-boudallaa/smart-data-pipeline-pfe) |

Les résultats chiffrés proviennent de tests en local ou de données simulées, comme indiqué dans le README de chaque dépôt.

---

## Ce que je recherche

Un poste **MLOps / AIOps Engineer** pour faire le lien entre le développement des modèles ML et leur mise en production : déploiement, CI/CD, monitoring et fiabilité.

## En cours d'apprentissage

Je travaille sur les compétences qui me manquent encore pour ce métier :
- [ ] Suivi d'expériences et registre de modèles avec **MLflow**
- [ ] Détection de **drift** des données et du modèle (Evidently)
- [ ] CI/CD qui teste, construit et déploie un modèle
- [ ] **Kubernetes**, Linux / Bash et orchestration (Airflow)

## Me contacter

Ouverte aux stages et opportunités en MLOps, AIOps, Data Engineering et IA.
Écrivez-moi par [e-mail](mailto:samahboudallaa@gmail.com) ou sur [LinkedIn](https://www.linkedin.com/in/samahboudallaa-92409a329).
