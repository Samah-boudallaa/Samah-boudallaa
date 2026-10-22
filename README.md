<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1f6feb,100:7c3aed&height=180&section=header&text=Samah%20Boudallaa&fontSize=46&fontColor=ffffff&fontAlignY=40" alt="Samah Boudallaa" width="100%"/>

<h3>Bachelor Sciences des Données · Data Engineering · Machine Learning &amp; IA</h3>

<p>
Étudiante à l'<b>Université Cadi Ayyad</b>, je conçois des solutions de bout en bout :<br/>
de la donnée brute au modèle exposé par une API, avec des tests, des conteneurs et un suivi des performances.<br/>
Je m'intéresse particulièrement aux <b>pipelines fiables</b>, à la <b>qualité logicielle</b> et à l'<b>industrialisation des solutions data</b>.
</p>

<a href="https://samah-boudallaa.github.io/"><img src="https://img.shields.io/badge/Portfolio-samah--boudallaa.github.io-1f6feb?style=for-the-badge&logo=githubpages&logoColor=white" alt="Portfolio"/></a>
<a href="https://www.linkedin.com/in/samah-boudallaa-92409a329"><img src="https://img.shields.io/badge/LinkedIn-Samah%20Boudallaa-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
<a href="mailto:samahboudallaa@gmail.com"><img src="https://img.shields.io/badge/E--mail-samahboudallaa%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="E-mail"/></a>
<img src="https://img.shields.io/badge/Localisation-Maroc-2E7D32?style=for-the-badge&logo=googlemaps&logoColor=white" alt="Maroc"/>

<br/><br/>

<b>Ouverte aux stages et aux opportunités en data engineering, machine learning et IA.</b>

</div>

<br/>

## Projets

<table>
<tr>

<td valign="top" width="33%">

<h3>01 · Smart Data Pipeline</h3>
<b>Pipeline IoT temps réel avec traitement adaptatif et supervision</b>
<br/><sub>Projet de fin d'études du DUT · équipe de trois · 2026</sub>

<br/><br/>
<b>Résultats clés (tests locaux)</b>
<ul>
<li>Environ <b>132 000</b> mesures simulées dans le flux</li>
<li><b>8</b> métriques de supervision Prometheus</li>
<li><b>6</b> conteneurs orchestrés avec Docker Compose</li>
<li>Latence inférieure à <b>500 ms</b> par message</li>
<li>Plus de <b>28 400</b> messages traités sans perte</li>
</ul>

<b>Stack</b><br/>
<code>Python</code> <code>Kafka</code> <code>Spark</code> <code>Pandas</code> <code>Isolation Forest</code> <code>Prometheus</code> <code>Grafana</code> <code>Docker Compose</code>

<br/><br/>
<a href="https://github.com/Samah-boudallaa/smart-data-pipeline-pfe"><img src="https://img.shields.io/badge/Voir%20le%20d%C3%A9p%C3%B4t-smart--data--pipeline--pfe-181717?style=for-the-badge&logo=github&logoColor=white" alt="Dépôt Smart Data Pipeline"/></a>

</td>

<td valign="top" width="33%">

<h3>02 · NexaDecide</h3>
<b>Plateforme d'aide à la décision intégrant data engineering et IA</b>
<br/><sub>Stage chez D-Business Consulting · avril – juin 2026</sub>

<br/><br/>
<b>Résultats clés (conditions des tests)</b>
<ul>
<li><b>443 154</b> enregistrements traités par le pipeline ETL</li>
<li>Cache lu en <b>moins de 100 ms</b> (contre 15 à 30 s en direct sur SQL Server)</li>
<li><b>9</b> endpoints FastAPI et <b>10</b> pages Streamlit</li>
<li>Prévision du CA : <b>MAPE de 8,9 %</b> (XGBoost, données simulées)</li>
<li>Recommandations Mistral AI, LangChain et RAG</li>
<li>Intégration Odoo CRM via XML-RPC (instance de test)</li>
</ul>

<b>Stack</b><br/>
<code>Python</code> <code>FastAPI</code> <code>Streamlit</code> <code>DuckDB</code> <code>Parquet</code> <code>XGBoost</code> <code>LangChain</code> <code>Mistral AI</code>

<br/><br/>
<a href="https://github.com/Samah-boudallaa/nexadecide-decision-system"><img src="https://img.shields.io/badge/Voir%20le%20d%C3%A9p%C3%B4t-nexadecide--decision--system-181717?style=for-the-badge&logo=github&logoColor=white" alt="Dépôt NexaDecide"/></a>

</td>

<td valign="top" width="33%">

<h3>03 · GraphGen</h3>
<b>Application web d'analyse exploratoire de fichiers CSV et Excel</b>
<br/><sub>Projet en binôme avec <a href="https://github.com/Chaymae-El-Bahloul">Chaymae El Bahloul</a></sub>

<br/><br/>
<b>Résultats clés</b>
<ul>
<li>Visualisations interactives avec <b>Plotly</b></li>
<li><b>12</b> tests pytest</li>
<li>Linting avec ruff</li>
<li>Intégration continue via GitHub Actions</li>
<li>Conteneur Docker <b>non-root</b> avec healthcheck</li>
</ul>

<b>Stack</b><br/>
<code>Python</code> <code>Flask</code> <code>Pandas</code> <code>Plotly</code> <code>pytest</code> <code>ruff</code> <code>GitHub Actions</code> <code>Docker</code>

<br/><br/>
<a href="https://github.com/Samah-boudallaa/GraphGen"><img src="https://img.shields.io/badge/Voir%20le%20d%C3%A9p%C3%B4t-GraphGen-181717?style=for-the-badge&logo=github&logoColor=white" alt="Dépôt GraphGen"/></a>

</td>

</tr>
</table>

<sub><i>Note sur les résultats : les métriques chiffrées proviennent de tests locaux ou de données simulées. Elles ne constituent pas des garanties de performance en production.</i></sub>

<br/>

### Architectures

<details>
<summary><b>01 · Smart Data Pipeline</b> — flux IoT temps réel, détection d'anomalies et supervision</summary>

```mermaid
flowchart LR
    A["Mesures IoT simulées"] --> B["Apache Kafka<br/>KRaft"]
    B --> C["Moteur adaptatif<br/>Pandas / Spark"]
    C --> D["Isolation Forest<br/>Détection d'anomalies"]
    C --> E["Prometheus<br/>Métriques"]
    E --> F["Grafana<br/>Supervision"]
    D --> G["Résultats de détection"]
```

</details>

<details>
<summary><b>02 · NexaDecide</b> — de SQL Server à l'API, la prévision et le RAG</summary>

```mermaid
flowchart TD
    A["SQL Server"] --> B["Pipeline ETL"]
    B --> C["DuckDB / Parquet<br/>Cache analytique"]
    C --> D["API FastAPI"]
    D --> E["Interface Streamlit"]
    D --> F["Prévision du CA<br/>XGBoost"]
    D --> G["RAG<br/>LangChain / Mistral AI"]
    H["Odoo CRM<br/>XML-RPC · instance de test"] <--> D
```

</details>

<details>
<summary><b>03 · GraphGen</b> — analyse de fichiers, tests et CI/CD</summary>

```mermaid
flowchart LR
    A["Fichiers CSV / Excel"] --> B["Flask / Pandas"]
    B --> C["Analyse des données"]
    C --> D["Visualisations Plotly"]
    B --> E["Tests pytest"]
    E --> F["GitHub Actions"]
    B --> G["Docker<br/>Utilisateur non-root"]
```

</details>

<br/>

## Stack technique

| Domaine | Technologies |
|---|---|
| **Langages** | ![Python](https://img.shields.io/badge/Python-1f6feb?style=flat-square&logo=python&logoColor=white) ![SQL](https://img.shields.io/badge/SQL-1f6feb?style=flat-square&logo=postgresql&logoColor=white) ![R](https://img.shields.io/badge/R-1f6feb?style=flat-square&logo=r&logoColor=white) ![C](https://img.shields.io/badge/C-1f6feb?style=flat-square&logo=c&logoColor=white) |
| **Data Engineering** | ![Kafka](https://img.shields.io/badge/Kafka-2E7D32?style=flat-square&logo=apachekafka&logoColor=white) ![Spark](https://img.shields.io/badge/Spark-2E7D32?style=flat-square&logo=apachespark&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-2E7D32?style=flat-square&logo=pandas&logoColor=white) ![ETL](https://img.shields.io/badge/ETL-2E7D32?style=flat-square) ![DuckDB](https://img.shields.io/badge/DuckDB-2E7D32?style=flat-square&logo=duckdb&logoColor=white) ![Parquet](https://img.shields.io/badge/Parquet-2E7D32?style=flat-square&logo=apacheparquet&logoColor=white) ![SQL Server](https://img.shields.io/badge/SQL%20Server-2E7D32?style=flat-square&logo=microsoftsqlserver&logoColor=white) ![MySQL](https://img.shields.io/badge/MySQL-2E7D32?style=flat-square&logo=mysql&logoColor=white) |
| **Machine Learning & IA** | ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-6A1B9A?style=flat-square&logo=scikitlearn&logoColor=white) ![XGBoost](https://img.shields.io/badge/XGBoost-6A1B9A?style=flat-square) ![Isolation Forest](https://img.shields.io/badge/Isolation%20Forest-6A1B9A?style=flat-square) ![RAG](https://img.shields.io/badge/RAG-6A1B9A?style=flat-square) ![LangChain](https://img.shields.io/badge/LangChain-6A1B9A?style=flat-square&logo=langchain&logoColor=white) ![Mistral AI](https://img.shields.io/badge/Mistral%20AI-6A1B9A?style=flat-square&logo=mistralai&logoColor=white) |
| **API & applications** | ![FastAPI](https://img.shields.io/badge/FastAPI-E65100?style=flat-square&logo=fastapi&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-E65100?style=flat-square&logo=flask&logoColor=white) ![REST](https://img.shields.io/badge/REST-E65100?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-E65100?style=flat-square&logo=streamlit&logoColor=white) |
| **Qualité & exploitation** | ![Docker](https://img.shields.io/badge/Docker-37474F?style=flat-square&logo=docker&logoColor=white) ![Docker Compose](https://img.shields.io/badge/Docker%20Compose-37474F?style=flat-square&logo=docker&logoColor=white) ![Git](https://img.shields.io/badge/Git-37474F?style=flat-square&logo=git&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-37474F?style=flat-square&logo=githubactions&logoColor=white) ![pytest](https://img.shields.io/badge/pytest-37474F?style=flat-square&logo=pytest&logoColor=white) ![ruff](https://img.shields.io/badge/ruff-37474F?style=flat-square&logo=ruff&logoColor=white) ![Prometheus](https://img.shields.io/badge/Prometheus-37474F?style=flat-square&logo=prometheus&logoColor=white) ![Grafana](https://img.shields.io/badge/Grafana-37474F?style=flat-square&logo=grafana&logoColor=white) |

<sub><i>Technologies utilisées dans des contextes variés, avec des niveaux de pratique différents.</i></sub>

<br/>

## Parcours

| Période | Intitulé | Détail |
|---|---|---|
| **2026 – en cours** | **Bachelor Sciences des Données** | EST Kelâa des Sraghna (Université Cadi Ayyad) |
| **2024 – 2026** | **DUT Ingénierie des Données** | EST Kelâa des Sraghna |
| **2025 – 2026** | **Trois stages** | Développement d'applications (été 2025) · Data engineering et IA (avril – juin 2026) · Data et BI (juin – août 2026) |
| **2024** | **Baccalauréat scientifique** | Mention Très Bien |

<br/>

<table>
<tr>

<td valign="top" width="50%">

<h3>En cours d'exploration</h3>
<sub>Sujets que j'apprends activement, pas encore pratiqués en production.</sub>
<ul>
<li>Suivi d'expériences et versioning des modèles avec <b>MLflow</b></li>
<li>Détection de dérive des données et des modèles</li>
<li><b>CI/CD</b> appliqué au machine learning</li>
<li><b>Kubernetes</b>, Linux et Bash</li>
</ul>

</td>

<td valign="top" width="50%">

<h3>Me contacter</h3>
<sub>Ouverte aux stages et aux opportunités en data engineering, machine learning et IA.</sub>
<br/><br/>
<a href="https://samah-boudallaa.github.io/"><img src="https://img.shields.io/badge/Portfolio-1f6feb?style=for-the-badge&logo=githubpages&logoColor=white" alt="Portfolio"/></a>
<a href="https://www.linkedin.com/in/samah-boudallaa-92409a329"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
<a href="mailto:samahboudallaa@gmail.com"><img src="https://img.shields.io/badge/E--mail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="E-mail"/></a>

</td>

</tr>
</table>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7c3aed,100:1f6feb&height=120&section=footer&text=Merci%20pour%20votre%20visite&fontSize=22&fontColor=ffffff&fontAlignY=45" alt="Merci pour votre visite" width="100%"/>

</div>
