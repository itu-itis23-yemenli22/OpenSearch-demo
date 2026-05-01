# OpenSearch Demo — YZV 322E

> AWS's open-source search and analytics engine — the free fork of Elasticsearch.

## 1. What is this tool?

OpenSearch is an open-source search and analytics engine developed by Amazon Web Services in 2021. It was forked from the last Apache 2.0-licensed version of Elasticsearch and is used for full-text search, log analysis, and real-time data visualization. It ships with OpenSearch Dashboards, a Kibana-equivalent visual interface for exploring and visualizing indexed data.

## 2. Prerequisites

- Docker Desktop ≥ 24.0
- Docker Compose ≥ 2.0
- Python ≥ 3.8 (for the example script)
- RAM: at least 4 GB free (OpenSearch is memory-intensive)
- OS: macOS, Windows, or Linux

## 3. Installation

```bash
# Clone the repository
git clone https://github.com/itu-itis23-yemenli22/OpenSearch-demo.git
cd OpenSearch-demo

# Start the services (first run will download ~500 MB of images)
docker compose up -d

# Wait ~30 seconds, then verify OpenSearch is running:
# Open http://localhost:9200 in your browser
# You should see a JSON response with "The OpenSearch Project" tagline
```

## 4. Running the example

```bash
# Install the required Python library
pip install requests

# Load sample data and run example queries
python load_data.py
```

## 5. Expected output

```
[1] Creating index...
  Status: 200 — True

[2] Loading books...
  Dune                                → 201
  1984                                → 201
  ...

==================================================
  Filter → genre = dystopia
==================================================
  3 results found:

  • 1984 (1949) — George Orwell  ★9.0
  • Brave New World (1932) — Aldous Huxley  ★8.7
  • Fahrenheit 451 (1953) — Ray Bradbury  ★8.5

✅ Demo complete! Open Dashboards at: http://localhost:5601
```

After running the script, open `http://localhost:5601` in your browser to explore the data visually using OpenSearch Dashboards.

## 6. Stopping the services

```bash
# Stop services (data is preserved)
docker compose down

# Stop services and delete all data
docker compose down -v
```

## 7. AI usage disclosure

Claude (Anthropic) was used during the preparation of this project for the following purposes:

- Generating the initial `docker-compose.yml` configuration template
- Creating the skeleton of the `load_data.py` script
- Drafting the README structure

All generated content was reviewed, tested, and adjusted where necessary. No unreviewed AI-generated output was submitted directly.
