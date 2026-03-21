from tkinter import INSERT

import psycopg2
import json
import os
with open("sample.json") as f:
    data = json.load(f)
batsmen = data["scorecard"][0]["batsman"]
bowlers = data["scorecard"][0]["bowler"]
fow = data["scorecard"][0]["fow"]["fow"]

conn = psycopg2.connect(
    host="localhost",
    database="cricket",
    user="postgres",
    password=os.environ.get("DB_PASSWORD")
)

print("Connected!")

scores = []
print(len(batsmen))
for player in batsmen:
    if player["sixes"] > 0 or player["fours"] > 0:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO batsmen (name, fours, sixes, strkrate) VALUES (%s, %s, %s, %s) ON CONFLICT (name) DO NOTHING;",
            (player["name"], player["fours"], player["sixes"], player["strkrate"])
        )
        conn.commit()
def get_batsmen():
    cursor=conn.cursor()
    cursor.execute("SELECT name,fours,sixes,strkrate FROM batsmen")
    return cursor.fetchall()
print(get_batsmen())




for name, score in scores:
    print(name, score)