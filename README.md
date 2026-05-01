# OpenSearch Demo — YZV 322E

> AWS'nin açık kaynak arama ve analitik motoru — Elasticsearch'ün özgür fork'u.

## 1. Bu araç nedir?

OpenSearch, Amazon Web Services tarafından 2021 yılında geliştirilen açık kaynaklı bir arama ve analitik motorudur. Elasticsearch'ün Apache 2.0 lisanslı son sürümünden türetilmiş olup tam metin arama, log analizi ve gerçek zamanlı veri görselleştirme için kullanılır. OpenSearch Dashboards aracılığıyla Kibana'ya eşdeğer bir görsel arayüz sunar.

## 2. Gereksinimler

- Docker Desktop ≥ 24.0
- Docker Compose ≥ 2.0
- Python ≥ 3.8 (örnek script için)
- RAM: en az 4 GB boş bellek (OpenSearch bellek yoğun)
- İşletim sistemi: macOS, Windows, Linux

## 3. Kurulum

```bash
# Repoyu klonla
git clone https://github.com/KULLANICI_ADIN/opensearch-demo.git
cd opensearch-demo

# Servisleri başlat (ilk indirmede birkaç dakika sürer)
docker compose up -d

# Servislerin hazır olmasını bekle (~30 saniye)
# Hazır olduğunu kontrol et:
curl http://localhost:9200 -u admin:Admin@1234!
```

Beklenen çıktı (kısaltılmış):
```json
{
  "name" : "opensearch",
  "cluster_name" : "docker-cluster",
  "version" : { "number" : "2.13.0", ... }
}
```

## 4. Örneği çalıştır

```bash
# Bağımlılıkları yükle
pip install requests

# Veri yükle ve sorguları çalıştır
python load_data.py
```

## 5. Beklenen çıktı

```
[1] Index oluşturuluyor...
  Durum: 200 — True

[2] Kitaplar yükleniyor...
  Dune                                → 201
  1984                                → 201
  ...

==================================================
  Filtre → genre = dystopia
==================================================
  3 sonuç bulundu:

  • 1984 (1949) — George Orwell  ★9.0
  • Brave New World (1932) — Aldous Huxley  ★8.7
  • Fahrenheit 451 (1953) — Ray Bradbury  ★8.5

✅ Demo tamamlandı! Dashboards için: http://localhost:5601
```

Tarayıcıda `http://localhost:5601` adresini aç → görsel dashboard arayüzüne ulaşırsın.

## 6. Servisleri durdur

```bash
docker compose down          # servisleri durdur (veri korunur)
docker compose down -v       # servisleri durdur + veriyi sil
```

## 7. AI kullanım beyanı

Bu proje hazırlanırken Claude (Anthropic) aşağıdaki amaçlarla kullanılmıştır:

- `docker-compose.yml` yapılandırması için başlangıç şablonu oluşturma
- `load_data.py` script iskeletinin hazırlanması
- README taslağının oluşturulması

Tüm içerik incelenerek, test edilerek ve gerekli yerlerde düzenlenerek kullanılmıştır. Gözden geçirilmemiş AI çıktısı doğrudan teslim edilmemiştir.
