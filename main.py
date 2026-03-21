from fastapi import FastAPI
import json
import os
import redis
from database import get_batsmen

app = FastAPI()

# Redis setup (optional)
redis_url = os.environ.get("REDIS_URL")

try:
    r = redis.from_url(redis_url) if redis_url else None
    if r:
        r.ping()
except:
    r = None


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/highlights")
def get_highlights():
    batsmen = None

    if r:
        try:
            cached = r.get("batsmen")
            if cached:
                batsmen = json.loads(cached)
        except Exception:
            batsmen = None

    if not batsmen:
        try:
            batsmen = get_batsmen()
        except Exception as e:
            return {"error": str(e)}

        if r:
            try:
                r.set("batsmen", json.dumps(batsmen))
            except Exception:
                pass

    scores = []
    for player in batsmen:
        try:
            name = player[0]
            sixes = int(player[1])
            fours = int(player[2])
            strike_rate = float(player[3])

            if sixes > 0 or fours > 0:
                excitement = sixes * 10 + fours * 5 + strike_rate / 10
                scores.append((name, excitement))
        except Exception:
            continue

    return {
    "top_batsmen": [
        {"name": name, "score": score}
        for name, score in scores
    ]
}