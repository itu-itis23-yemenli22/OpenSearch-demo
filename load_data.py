"""
OpenSearch Demo — Örnek Veri Yükleyici
--------------------------------------
Bu script OpenSearch'e 10 adet kitap verisi ekler,
ardından birkaç örnek arama sorgusu çalıştırır.

Kullanım:
    pip install requests
    python load_data.py
"""

import requests
import json

BASE_URL = "http://localhost:9200"
INDEX = "books"
AUTH = ("admin", "Admin@1234!")  # docker-compose'daki şifreyle aynı

# ── Örnek veri ──────────────────────────────────────────────────────────────

BOOKS = [
    {"title": "Dune", "author": "Frank Herbert", "year": 1965, "genre": "sci-fi", "rating": 9.2},
    {"title": "1984", "author": "George Orwell", "year": 1949, "genre": "dystopia", "rating": 9.0},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932, "genre": "dystopia", "rating": 8.7},
    {"title": "Foundation", "author": "Isaac Asimov", "year": 1951, "genre": "sci-fi", "rating": 8.9},
    {"title": "Neuromancer", "author": "William Gibson", "year": 1984, "genre": "sci-fi", "rating": 8.3},
    {"title": "The Hitchhiker's Guide", "author": "Douglas Adams", "year": 1979, "genre": "comedy", "rating": 8.8},
    {"title": "Fahrenheit 451", "author": "Ray Bradbury", "year": 1953, "genre": "dystopia", "rating": 8.5},
    {"title": "Snow Crash", "author": "Neal Stephenson", "year": 1992, "genre": "sci-fi", "rating": 8.4},
    {"title": "The Left Hand of Darkness", "author": "Ursula K. Le Guin", "year": 1969, "genre": "sci-fi", "rating": 8.6},
    {"title": "Do Androids Dream of Electric Sheep?", "author": "Philip K. Dick", "year": 1968, "genre": "sci-fi", "rating": 8.5},
]

# ── Yardımcı fonksiyonlar ────────────────────────────────────────────────────

def print_result(label, response):
    print(f"\n{'='*50}")
    print(f"  {label}")
    print(f"{'='*50}")
    data = response.json()
    if "hits" in data:
        hits = data["hits"]["hits"]
        print(f"  {len(hits)} sonuç bulundu:\n")
        for h in hits:
            s = h["_source"]
            print(f"  • {s['title']} ({s['year']}) — {s['author']}  ★{s['rating']}")
    else:
        print(json.dumps(data, indent=2, ensure_ascii=False))

# ── 1. Index oluştur ─────────────────────────────────────────────────────────

print("\n[1] Index oluşturuluyor...")
r = requests.put(
    f"{BASE_URL}/{INDEX}",
    auth=AUTH,
    headers={"Content-Type": "application/json"},
    json={
        "mappings": {
            "properties": {
                "title":  {"type": "text"},
                "author": {"type": "keyword"},
                "year":   {"type": "integer"},
                "genre":  {"type": "keyword"},
                "rating": {"type": "float"},
            }
        }
    },
    verify=False
)
print(f"  Durum: {r.status_code} — {r.json().get('acknowledged', r.text)}")

# ── 2. Verileri yükle ────────────────────────────────────────────────────────

print("\n[2] Kitaplar yükleniyor...")
for i, book in enumerate(BOOKS):
    r = requests.post(
        f"{BASE_URL}/{INDEX}/_doc/{i+1}",
        auth=AUTH,
        headers={"Content-Type": "application/json"},
        json=book,
        verify=False
    )
    print(f"  {book['title'][:35]:<35} → {r.status_code}")

# OpenSearch'in index'i oluşturması için bekle
import time
time.sleep(1)

# ── 3. Örnek sorgular ────────────────────────────────────────────────────────

# Sorgu 1: Tam metin arama — "dream" geçen kitaplar
r = requests.get(
    f"{BASE_URL}/{INDEX}/_search",
    auth=AUTH,
    json={"query": {"match": {"title": "dream"}}},
    verify=False
)
print_result('Tam metin arama → title içinde "dream"', r)

# Sorgu 2: Filtre — sadece dystopia kitaplar
r = requests.get(
    f"{BASE_URL}/{INDEX}/_search",
    auth=AUTH,
    json={"query": {"term": {"genre": "dystopia"}}},
    verify=False
)
print_result("Filtre → genre = dystopia", r)

# Sorgu 3: Aralık — 1960 sonrası, rating > 8.5
r = requests.get(
    f"{BASE_URL}/{INDEX}/_search",
    auth=AUTH,
    json={
        "query": {
            "bool": {
                "filter": [
                    {"range": {"year":   {"gt": 1960}}},
                    {"range": {"rating": {"gte": 8.5}}},
                ]
            }
        },
        "sort": [{"rating": "desc"}]
    },
    verify=False
)
print_result("Karmaşık sorgu → 1960 sonrası, rating ≥ 8.5, puana göre sıralı", r)

print("\n✅ Demo tamamlandı! Dashboards için: http://localhost:5601\n")
