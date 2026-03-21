# 🏏 Cricket Highlights Detection API

Automatically identify the most exciting moments from a cricket match using a custom scoring algorithm.

---

## 🚀 Live API

https://web-production-27d62.up.railway.app/highlights

---

## 🧠 What It Does

* Processes cricket scorecard data
* Computes an **excitement score** for each batsman
* Returns the most impactful performances

---

## ⚡ Scoring Logic

```
score = (sixes × 10) + (fours × 5) + (strike_rate / 10)
```

* Six → 10 points
* Four → 5 points
* Strike rate → bonus factor

Only players with boundaries are considered.

---

## 🏗️ Architecture

```
Client Request
      ↓
FastAPI Backend
      ↓
PostgreSQL (Railway)
      ↓
Redis Cache (optional)
```

---

## 📊 Example Response

```json
{
  "top_batsmen": [
    {"name": "Stirling", "score": 20.0},
    {"name": "Balbirnie", "score": 40.0},
    {"name": "Lorcan Tucker", "score": 120.0}
  ]
}
```

---

## 🔧 Tech Stack

* Python
* FastAPI
* PostgreSQL (Railway)
* Redis (caching)
* Uvicorn

---

## ▶️ Run Locally

```bash
git clone https://github.com/Aadhithya0609/cricket_highlights
cd cricket_highlights

pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 🗄️ Database Setup

Create table:

```sql
CREATE TABLE batsmen (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE,
    fours INTEGER,
    sixes INTEGER,
    strkrate FLOAT
);
```

---

## 📥 Load Data

Run once to insert sample data:

```bash
python seed.py
```

Make sure `DATABASE_URL` is set.

---

## ⚠️ Notes

* Uses preloaded match data (not real-time yet)
* Redis is optional (fallback works without it)
* Designed for learning system design + scaling concepts

---

## 📈 Next Improvements

* Real-time ball-by-ball ingestion
* Event-driven pipeline (Kafka / Webhooks)
* Better ranking (top N, filtering)
* Distributed caching

---

## 👤 Author

Aadhithya A K
Final Year EEE — RMK Engineering College


---

## 📄 Case Study

Detailed system design and load testing analysis available separately.
