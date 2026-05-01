# OpenSearch Demo — YZV 322E

> AWS's open-source search and analytics engine — the free fork of Elasticsearch.

## 1. What is this tool?

OpenSearch is an open-source search and analytics engine developed by Amazon Web Services in 2021. It was forked from the last Apache 2.0-licensed version of Elasticsearch after Elastic changed its license to the more restrictive SSPL. OpenSearch is used for full-text search, log analysis, and real-time data visualization, and ships with OpenSearch Dashboards — a Kibana-equivalent visual interface — at no additional cost.

## 2. Prerequisites

| Requirement | Version |
|---|---|
| Docker Desktop | ≥ 24.0 |
| Docker Compose | ≥ 2.0 (included with Docker Desktop) |
| Python | ≥ 3.8 |
| pip | any recent version |
| RAM | at least 4 GB free (OpenSearch is memory-intensive) |
| OS | macOS, Windows, or Linux |

> **Note:** On Windows, make sure Docker Desktop is running before executing any `docker` commands.

## 3. Installation

```bash
# 1. Clone the repository
git clone https://github.com/itu-itis23-yemenli22/OpenSearch-demo.git
cd OpenSearch-demo

# 2. Start OpenSearch and OpenSearch Dashboards
docker compose up -d

# 3. Wait ~30 seconds for both services to initialize, then verify:
# Open http://localhost:9200 in your browser
# You should see a JSON response like this:
# {
#   "name" : "...",
#   "tagline" : "The OpenSearch Project: https://opensearch.org/"
# }

# 4. Open OpenSearch Dashboards
# Navigate to http://localhost:5601 in your browser
```

The `docker compose up -d` command starts two services defined in `docker-compose.yml`:
- **opensearch** — the search engine, accessible at port 9200
- **opensearch-dashboards** — the visual UI, accessible at port 5601

## 4. Running the example

```bash
# Install the required Python library
pip install requests

# Load sample data and run example queries
python load_data.py
```

This script does the following:
1. Creates a `books` index with fields: `title` (text), `author` (keyword), `genre` (keyword), `year` (integer), `rating` (float)
2. Loads 10 classic science fiction and dystopia novels
3. Runs 3 example queries: full-text search, filter query, and a complex boolean query with sorting

## 5. Expected output

Running `python load_data.py` should produce the following output:

```
[1] Creating index...
  Status: 200 — True

[2] Loading books...
  Dune                                → 201
  1984                                → 201
  Brave New World                     → 201
  Foundation                          → 201
  Neuromancer                         → 201
  The Hitchhiker's Guide              → 201
  Fahrenheit 451                      → 201
  Snow Crash                          → 201
  The Left Hand of Darkness           → 201
  Do Androids Dream of Electric Sheep? → 201

==================================================
  Full-text search → title contains "dream"
==================================================
  1 result found:

  • Do Androids Dream of Electric Sheep? (1968) — Philip K. Dick  ★8.5

==================================================
  Filter → genre = dystopia
==================================================
  3 results found:

  • 1984 (1949) — George Orwell  ★9.0
  • Brave New World (1932) — Aldous Huxley  ★8.7
  • Fahrenheit 451 (1953) — Ray Bradbury  ★8.5

==================================================
  Complex query → published after 1960, rating ≥ 8.5, sorted by rating
==================================================
  3 results found:

  • Dune (1965) — Frank Herbert  ★9.2
  • The Left Hand of Darkness (1969) — Ursula K. Le Guin  ★8.6
  • Do Androids Dream of Electric Sheep? (1968) — Philip K. Dick  ★8.5

✅ Demo complete! Open Dashboards at: http://localhost:5601
```

HTTP status codes explanation:
- `200` — index created successfully
- `201` — document indexed successfully

After running the script, open `http://localhost:5601` to explore the data visually:
- Go to **Discover** to browse and search all indexed books
- Go to **Visualize** to create charts (e.g. genre distribution pie chart)
- Go to **Dev Tools** to run raw OpenSearch queries interactively

## 6. Stopping the services

```bash
# Stop services but keep data
docker compose down

# Stop services and delete all stored data
docker compose down -v
```

## 7. AI usage disclosure

Claude was used during the preparation of this project for the following purposes:

- Researching and understanding OpenSearch concepts, architecture, and use cases
- Troubleshooting Docker configuration issues during setup
- Drafting and refining the README structure and wording

All code files were written, tested, and verified by the author. The demo environment was set up and run locally to confirm all instructions produce the expected output.
