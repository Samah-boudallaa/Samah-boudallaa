"""Single source of truth for project facts used by the generated graphics.

Every entry was checked against the public repository README / file tree
(see `source`). Do NOT add a capability here unless the repository shows it:
the constellation graphic is derived from this file, so an unverified entry
would become an unverified claim in the profile.
"""

USER = "Samah-boudallaa"

STAGES = [
    ("ingest", "Ingestion"),
    ("process", "Processing"),
    ("ml", "ML / AI"),
    ("api", "API"),
    ("test", "Testing & CI"),
    ("container", "Containers"),
    ("observe", "Observability"),
]

PROJECTS = {
    "SYSTEM_01": {
        "name": "Smart Data Pipeline",
        "repo": "smart-data-pipeline-pfe",
        "source": "https://github.com/Samah-boudallaa/smart-data-pipeline-pfe",
        "stages": {
            "ingest": "Apache Kafka 3.7 (KRaft)",
            "process": "Adaptive Pandas / Spark engine",
            "ml": "Isolation Forest anomaly detection",
            "container": "Docker Compose, 6 services",
            "observe": "Prometheus (8 metrics) + Grafana",
        },
    },
    "SYSTEM_02": {
        "name": "NexaDecide",
        "repo": "nexadecide-decision-system",
        "source": "https://github.com/Samah-boudallaa/nexadecide-decision-system",
        "stages": {
            "ingest": "ETL SQL Server to DuckDB / Parquet",
            "process": "Server-side aggregation, 120 min cache",
            "ml": "XGBoost (simulated data), RAG with LangChain + Mistral AI",
            "api": "FastAPI, 9 endpoints",
        },
    },
    "SYSTEM_03": {
        "name": "GraphGen",
        "repo": "GraphGen",
        "source": "https://github.com/Samah-boudallaa/GraphGen",
        "stages": {
            "process": "pandas profiling and correlations",
            "api": "Flask web application",
            "test": "12 pytest tests, ruff, GitHub Actions",
            "container": "Non-root Docker image with healthcheck",
        },
    },
}
