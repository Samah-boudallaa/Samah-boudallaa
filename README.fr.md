<p align="right"><sub><a href="./README.md" title="Read in English">EN</a> · <b>FR</b></sub></p>

<img src="./hero-fr.svg" alt="Samah Boudallaa, Data Engineering, Machine Learning et IA" width="100%"/>

<div align="center">

<br/>

<b>Étudiante en Data Science · Data Engineering, Machine Learning et IA</b><br/>
<sub>Maroc · ouverte aux stages en data engineering, machine learning et IA</sub>

<br/><br/>

<a href="https://samah-boudallaa.github.io/"><img src="https://img.shields.io/badge/Portfolio-samah--boudallaa.github.io-21262d?style=flat-square&logo=githubpages&logoColor=a371f7" alt="Portfolio"/></a>
<a href="https://www.linkedin.com/in/samah-boudallaa-92409a329"><img src="https://img.shields.io/badge/LinkedIn-Samah%20Boudallaa-21262d?style=flat-square&logo=linkedin&logoColor=a371f7" alt="LinkedIn"/></a>
<a href="mailto:samahboudallaa@gmail.com"><img src="https://img.shields.io/badge/E--mail-samahboudallaa%40gmail.com-21262d?style=flat-square&logo=gmail&logoColor=a371f7" alt="E-mail"/></a>
<a href="https://github.com/Samah-boudallaa"><img src="https://img.shields.io/badge/GitHub-Samah--boudallaa-21262d?style=flat-square&logo=github&logoColor=a371f7" alt="GitHub"/></a>

<br/><br/>

<sub><a href="#projets">Projets</a> &nbsp;·&nbsp; <a href="#architectures">Architectures</a> &nbsp;·&nbsp; <a href="#stack-technique">Stack</a> &nbsp;·&nbsp; <a href="#activité-github">Activité</a> &nbsp;·&nbsp; <a href="#parcours">Parcours</a> &nbsp;·&nbsp; <a href="#me-contacter">Contact</a></sub>

</div>

<br/>

## En 30 secondes

Étudiante en **Bachelor Sciences des Données** à l'EST de Kelâa des Sraghna (Université Cadi Ayyad), après un **DUT en Ingénierie des Données**. Je m'intéresse au **data engineering**, au **machine learning**, à l'**IA** et à l'**industrialisation des pipelines de données**.

> De la donnée brute au modèle exposé par une API, avec tests, conteneurs et suivi.

<table>
<tr>
<td valign="top" width="33%">
<b>Je cherche</b><br/>
Un stage en <b>data engineering</b>, <b>machine learning</b> ou <b>IA</b>, où la donnée finit réellement en production.
</td>
<td valign="top" width="33%">
<b>J'apporte</b><br/>
Des pipelines streaming et batch, des API, des tests, de la CI et des conteneurs : le tout <b>reproductible</b>.
</td>
<td valign="top" width="33%">
<b>À vérifier</b><br/>
Chaque projet ci-dessous a son dépôt public, son schéma d'architecture et des chiffres issus de tests locaux.
</td>
</tr>
</table>

<br/>

<div align="center">
<img src="./pipeline.svg" alt="Flux de données de bout en bout" width="100%"/>
</div>

<br/>

## Projets

<table>
<tr>
<td valign="top" width="46%">

<h3>Smart Data Pipeline</h3>
<b>Pipeline IoT temps réel avec traitement adaptatif et supervision</b>
<br/><sub>Projet de fin d'études du DUT · équipe de trois · 2026</sub>

<br/><br/>
<code>Python</code> <code>Kafka</code> <code>Spark</code> <code>Pandas</code> <code>Isolation Forest</code> <code>Prometheus</code> <code>Grafana</code> <code>Docker Compose</code>

<br/><br/>
<b><a href="https://github.com/Samah-boudallaa/smart-data-pipeline-pfe">Voir le dépôt</a></b>
<br/>
<img src="https://img.shields.io/github/last-commit/Samah-boudallaa/smart-data-pipeline-pfe?style=flat-square&label=dernier%20commit&color=7c3aed&labelColor=21262d" alt="dernier commit"/>

</td>
<td valign="top" width="54%">

<b>Résultats clés (tests locaux)</b>
<ul>
<li>Environ <b>132 000</b> mesures simulées dans le flux</li>
<li><b>8</b> métriques de supervision Prometheus</li>
<li><b>6</b> conteneurs orchestrés avec Docker Compose</li>
<li>Latence inférieure à <b>500 ms</b> par message</li>
<li>Plus de <b>28 400</b> messages traités sans perte</li>
</ul>

</td>
</tr>
</table>

<br/>

<table>
<tr>
<td valign="top" width="46%">

<h3>NexaDecide</h3>
<b>Plateforme d'aide à la décision intégrant data engineering et IA</b>
<br/><sub>Stage chez D-Business Consulting · avril – juin 2026</sub>

<br/><br/>
<code>Python</code> <code>FastAPI</code> <code>Streamlit</code> <code>DuckDB</code> <code>Parquet</code> <code>XGBoost</code> <code>LangChain</code> <code>Mistral AI</code>

<br/><br/>
<b><a href="https://github.com/Samah-boudallaa/nexadecide-decision-system">Voir le dépôt</a></b>
<br/>
<img src="https://img.shields.io/github/last-commit/Samah-boudallaa/nexadecide-decision-system?style=flat-square&label=dernier%20commit&color=7c3aed&labelColor=21262d" alt="dernier commit"/>

</td>
<td valign="top" width="54%">

<b>Résultats clés (conditions des tests)</b>
<ul>
<li><b>443 154</b> enregistrements traités par le pipeline ETL</li>
<li>Cache lu en <b>moins de 100 ms</b> (contre 15 à 30 s en direct sur SQL Server)</li>
<li><b>9</b> endpoints FastAPI et <b>10</b> pages Streamlit</li>
<li>Prévision du CA : <b>MAPE de 8,9 %</b> (XGBoost, données simulées)</li>
<li>Recommandations Mistral AI, LangChain et RAG</li>
<li>Intégration Odoo CRM via XML-RPC (instance de test)</li>
</ul>

</td>
</tr>
</table>

<br/>

<table>
<tr>
<td valign="top" width="46%">

<h3>GraphGen</h3>
<b>Application web d'analyse exploratoire de fichiers CSV et Excel</b>
<br/><sub>Projet en binôme avec <a href="https://github.com/Chaymae-El-Bahloul">Chaymae El Bahloul</a></sub>

<br/><br/>
<code>Python</code> <code>Flask</code> <code>Pandas</code> <code>Plotly</code> <code>pytest</code> <code>ruff</code> <code>GitHub Actions</code> <code>Docker</code>

<br/><br/>
<b><a href="https://github.com/Samah-boudallaa/GraphGen">Voir le dépôt</a></b>
<br/>
<a href="https://github.com/Samah-boudallaa/GraphGen/actions/workflows/ci.yml"><img src="https://github.com/Samah-boudallaa/GraphGen/actions/workflows/ci.yml/badge.svg" alt="Statut de la CI GraphGen"/></a>

</td>
<td valign="top" width="54%">

<b>Résultats clés</b>
<ul>
<li>Visualisations interactives avec <b>Plotly</b></li>
<li><b>12</b> tests pytest</li>
<li>Linting avec ruff</li>
<li>Intégration continue via GitHub Actions</li>
<li>Conteneur Docker <b>non-root</b> avec healthcheck</li>
</ul>

</td>
</tr>
</table>

<sub><i>Note sur les résultats : les métriques chiffrées proviennent de tests locaux ou de données simulées. Elles ne constituent pas des garanties de performance en production.</i></sub>

<br/>

<details>
<summary><b>Pourquoi ces projets ? Ce qu'ils montrent de ma façon de travailler</b></summary>

<br/>

| Projet | Compétence démontrée | Preuve dans le dépôt |
|---|---|---|
| **Smart Data Pipeline** | Concevoir un flux temps réel observable | Kafka, métriques Prometheus, tableaux de bord Grafana, `docker-compose.yml` |
| **NexaDecide** | Relier données, modèles et usages métier | ETL, cache DuckDB/Parquet, API FastAPI, prévision, RAG |
| **GraphGen** | Livrer un logiciel propre et reproductible | Tests pytest, ruff, CI GitHub Actions, image Docker non-root |

</details>

<br/>

## Architectures

<sub>Cliquez sur un projet pour déplier son schéma.</sub>

<details>
<summary><b>Smart Data Pipeline</b>, flux IoT temps réel, détection d'anomalies et supervision</summary>

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#1c1730","primaryTextColor":"#e6edf3","primaryBorderColor":"#7c3aed","lineColor":"#a371f7","secondaryColor":"#1c1730","tertiaryColor":"#0d1117","fontSize":"14px"}}}%%
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
<summary><b>NexaDecide</b>, de SQL Server à l'API, la prévision et le RAG</summary>

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#1c1730","primaryTextColor":"#e6edf3","primaryBorderColor":"#7c3aed","lineColor":"#a371f7","secondaryColor":"#1c1730","tertiaryColor":"#0d1117","fontSize":"14px"}}}%%
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
<summary><b>GraphGen</b>, analyse de fichiers, tests et CI/CD</summary>

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#1c1730","primaryTextColor":"#e6edf3","primaryBorderColor":"#7c3aed","lineColor":"#a371f7","secondaryColor":"#1c1730","tertiaryColor":"#0d1117","fontSize":"14px"}}}%%
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
| **Langages** | ![Python](https://img.shields.io/badge/Python-21262d?style=flat-square&logo=python&logoColor=a371f7) ![SQL](https://img.shields.io/badge/SQL-21262d?style=flat-square&logo=postgresql&logoColor=a371f7) ![R](https://img.shields.io/badge/R-21262d?style=flat-square&logo=r&logoColor=a371f7) ![C](https://img.shields.io/badge/C-21262d?style=flat-square&logo=c&logoColor=a371f7) |
| **Data Engineering** | ![Kafka](https://img.shields.io/badge/Kafka-21262d?style=flat-square&logo=apachekafka&logoColor=a371f7) ![Spark](https://img.shields.io/badge/Spark-21262d?style=flat-square&logo=apachespark&logoColor=a371f7) ![Pandas](https://img.shields.io/badge/Pandas-21262d?style=flat-square&logo=pandas&logoColor=a371f7) ![ETL](https://img.shields.io/badge/ETL-21262d?style=flat-square) ![DuckDB](https://img.shields.io/badge/DuckDB-21262d?style=flat-square&logo=duckdb&logoColor=a371f7) ![Parquet](https://img.shields.io/badge/Parquet-21262d?style=flat-square&logo=apacheparquet&logoColor=a371f7) ![SQL Server](https://img.shields.io/badge/SQL%20Server-21262d?style=flat-square&logo=microsoftsqlserver&logoColor=a371f7) ![MySQL](https://img.shields.io/badge/MySQL-21262d?style=flat-square&logo=mysql&logoColor=a371f7) |
| **Machine Learning et IA** | ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-21262d?style=flat-square&logo=scikitlearn&logoColor=a371f7) ![XGBoost](https://img.shields.io/badge/XGBoost-21262d?style=flat-square) ![Isolation Forest](https://img.shields.io/badge/Isolation%20Forest-21262d?style=flat-square) ![RAG](https://img.shields.io/badge/RAG-21262d?style=flat-square) ![LangChain](https://img.shields.io/badge/LangChain-21262d?style=flat-square&logo=langchain&logoColor=a371f7) ![Mistral AI](https://img.shields.io/badge/Mistral%20AI-21262d?style=flat-square&logo=mistralai&logoColor=a371f7) |
| **API et applications** | ![FastAPI](https://img.shields.io/badge/FastAPI-21262d?style=flat-square&logo=fastapi&logoColor=a371f7) ![Flask](https://img.shields.io/badge/Flask-21262d?style=flat-square&logo=flask&logoColor=a371f7) ![REST](https://img.shields.io/badge/REST-21262d?style=flat-square) ![Streamlit](https://img.shields.io/badge/Streamlit-21262d?style=flat-square&logo=streamlit&logoColor=a371f7) |
| **Qualité et exploitation** | ![Docker](https://img.shields.io/badge/Docker-21262d?style=flat-square&logo=docker&logoColor=a371f7) ![Docker Compose](https://img.shields.io/badge/Docker%20Compose-21262d?style=flat-square&logo=docker&logoColor=a371f7) ![Git](https://img.shields.io/badge/Git-21262d?style=flat-square&logo=git&logoColor=a371f7) ![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-21262d?style=flat-square&logo=githubactions&logoColor=a371f7) ![pytest](https://img.shields.io/badge/pytest-21262d?style=flat-square&logo=pytest&logoColor=a371f7) ![ruff](https://img.shields.io/badge/ruff-21262d?style=flat-square&logo=ruff&logoColor=a371f7) ![Prometheus](https://img.shields.io/badge/Prometheus-21262d?style=flat-square&logo=prometheus&logoColor=a371f7) ![Grafana](https://img.shields.io/badge/Grafana-21262d?style=flat-square&logo=grafana&logoColor=a371f7) |

<sub><i>Technologies utilisées dans des contextes variés, avec des niveaux de pratique différents.</i></sub>

<br/>

## Activité GitHub

Ce tableau de bord n'est pas un widget tiers : il est **généré chaque jour par mon propre pipeline** (script Python + GitHub Actions) à partir de l'API GitHub. Un pipeline de données, appliqué à mon propre profil.

<div align="center">

<img src="./stats.svg" alt="Tableau de bord GitHub généré automatiquement" width="100%"/>

<sub><i>Une part du travail de stage est dans des dépôts privés : selon le jeton utilisé, elle est comptée à part ou absente de ces graphiques.<br/>La page du profil GitHub, elle, additionne les contributions publiques et privées.</i></sub>

</div>

<details>
<summary><b>Vue 3D des contributions</b></summary>

<br/>

<div align="center">
<img src="./profile-3d-contrib/profile-night-view.svg" alt="Contributions GitHub en 3D" width="100%"/>
<br/>
<sub><i>Générée par GitHub Actions avec l'action open source github-profile-3d-contrib.</i></sub>
</div>

</details>

<details>
<summary><b>Comment ce tableau de bord est produit</b></summary>

<br/>

Rien n'est copié à la main : un workflow GitHub Actions interroge l'API GitHub (REST et GraphQL), un script Python calcule les indicateurs et écrit des fichiers SVG animés, puis le résultat est commité automatiquement.

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#1c1730","primaryTextColor":"#e6edf3","primaryBorderColor":"#7c3aed","lineColor":"#a371f7","secondaryColor":"#1c1730","tertiaryColor":"#0d1117","fontSize":"14px"}}}%%
flowchart LR
    A["GitHub Actions<br/>exécution planifiée"] --> B["Script Python<br/>API REST + GraphQL"]
    B --> C["stats.svg<br/>tableau de bord animé"]
    A --> E["Vue 3D<br/>contributions"]
    C --> F["README du profil"]
    E --> F
```

</details>

<br/>

## Parcours

| Période | Intitulé | Détail |
|---|---|---|
| **2026 – en cours** | **Bachelor Sciences des Données** | EST Kelâa des Sraghna (Université Cadi Ayyad) |
| **2024 – 2026** | **DUT Ingénierie des Données** | EST Kelâa des Sraghna |
| **2025 – 2026** | **Trois stages** | Développement d'applications (été 2025) · Data engineering et IA (avril – juin 2026) · Data et BI (juin – août 2026) |
| **2024** | **Baccalauréat scientifique** | Mention Très Bien |

<details>
<summary><b>Voir la frise chronologique</b></summary>

```mermaid
%%{init: {"theme":"base","themeVariables":{"primaryColor":"#1c1730","primaryTextColor":"#e6edf3","primaryBorderColor":"#7c3aed","lineColor":"#a371f7","secondaryColor":"#1c1730","tertiaryColor":"#0d1117","fontSize":"14px"}}}%%
timeline
    title Mon parcours
    2024 : Baccalauréat scientifique (Mention Très Bien)
         : Entrée au DUT Ingénierie des Données · EST Kelâa des Sraghna
    2025 : Stage développement d'applications (été)
    2026 : PFE Smart Data Pipeline
         : Stage data engineering et IA · D-Business Consulting (avril – juin)
         : Stage data et BI (juin – août)
         : Bachelor Sciences des Données · Université Cadi Ayyad
```

</details>

<br/>

## En cours d'exploration

<sub>Sujets que j'apprends activement, pas encore pratiqués en production.</sub>

- Suivi d'expériences et versioning des modèles avec **MLflow**
- Détection de dérive des données et des modèles
- **CI/CD** appliqué au machine learning
- **Kubernetes**, Linux et Bash

<br/>

## Me contacter

Ouverte aux stages et aux opportunités en data engineering, machine learning et IA.

<table>
<tr><td><b>Portfolio</b></td><td><a href="https://samah-boudallaa.github.io/">samah-boudallaa.github.io</a></td></tr>
<tr><td><b>LinkedIn</b></td><td><a href="https://www.linkedin.com/in/samah-boudallaa-92409a329">Samah Boudallaa</a></td></tr>
<tr><td><b>E-mail</b></td><td><a href="mailto:samahboudallaa@gmail.com">samahboudallaa@gmail.com</a></td></tr>
<tr><td><b>GitHub</b></td><td><a href="https://github.com/Samah-boudallaa">Samah-boudallaa</a></td></tr>
</table>

<br/>

<details>
<summary><sub>docker compose up -d</sub></summary>

<br/>

```bash
$ docker compose up -d
[+] Running 6/6
 Container kafka         Started
 Container spark         Started
 Container anomaly-ml    Started
 Container prometheus    Started
 Container grafana       Started
 Container samah         Started   # recrutez-moi
```

</details>

<br/>

<div align="center">

<img src="./divider.svg" alt="" width="100%"/>

<br/>

Merci pour votre visite. Une question, un projet, un stage : écrivez-moi.

<sub><a href="https://samah-boudallaa.github.io/">Portfolio</a> · <a href="https://www.linkedin.com/in/samah-boudallaa-92409a329">LinkedIn</a> · <a href="mailto:samahboudallaa@gmail.com">E-mail</a> · <a href="https://github.com/Samah-boudallaa">GitHub</a></sub>

<br/>

<sub><a href="./README.md" title="Read in English">EN</a> · <b>FR</b></sub>

</div>
