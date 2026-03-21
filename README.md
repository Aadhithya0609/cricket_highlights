# 🏏 Cricket Highlights Detection API

Automatically identify the most exciting moments from a cricket match.

---

## 🚀 Live API

https://web-production-27d62.up.railway.app/highlights

Hit the endpoint → get highlights from real match data.

---

## 🧠 What It Does

* Processes a cricket scorecard (Cricbuzz data)
* Scores players using an **excitement scoring algorithm**
* Extracts key highlights:

  * Top batsmen
  * Key wicket moments

---

## ⚡ Excitement Scoring

```
score = (sixes × 10) + (fours × 5) + (strike_rate / 10)
```

* Six → 10 points
* Wicket → 10 points
* Four → 5 points
* Strike rate → bonus

Simple, explainable, and based on cricket intuition.

---

## 🏗️ Architecture

```
Cricbuzz API / JSON
        ↓
Python Scoring Engine
        ↓
PostgreSQL
        ↓
FastAPI (/highlights)
        ↓
Users
```

---

## 📊 Load Testing

Tested using Locust.

| Users | Median | 99th %ile | Failures |
| ----- | ------ | --------- | -------- |
| 100   | 9 ms   | 1954 ms   | 0%       |
| 500   | 9 ms   | 120 ms    | 0%       |
| 1000  | —      | —         | 72% ❌    |

* Breaking point: **~280 concurrent users**
* Improvement at 500 users due to **in-memory caching**

---

## 🔧 Tech Stack

* FastAPI — API layer
* PostgreSQL — data storage
* Locust — load testing
* Railway — deployment

---

## ▶️ Run Locally

```bash
git clone https://github.com/Aadhithya0609/cricket_highlights
cd cricket_highlights

pip install -r requirements.txt
uvicorn main:app --reload
```

Load testing:

```bash
locust -f locustfile.py --host=http://127.0.0.1:8000
```

---

## ⚠️ Limitations

* Not real-time (uses static match data)
* Single-server deployment
* No distributed caching
* No horizontal scaling yet

---

## 📈 Next Steps

* Add Redis caching
* Introduce load balancing
* Move to event-driven ingestion (webhooks)

---

## 👤 Author

Aadhithya A K
Final Year EEE — RMK Engineering College


---

## 📄 Case Study

Detailed case study available in `/docs` (or on request).
