import psycopg2
import os
import json

DATABASE_URL = os.environ.get("DATABASE_URL")


def get_connection():
    return psycopg2.connect(DATABASE_URL)


def insert_batsmen():
    with open("sample.json") as f:
        data = json.load(f)

    batsmen = data["scorecard"][0]["batsman"]

    conn = get_connection()
    cursor = conn.cursor()

    for player in batsmen:
        if player["sixes"] > 0 or player["fours"] > 0:
            cursor.execute(
                """
                INSERT INTO batsmen (name, fours, sixes, strkrate)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (name) DO NOTHING;
                """,
                (
                    player["name"],
                    player["fours"],
                    player["sixes"],
                    player["strkrate"]
                )
            )

    conn.commit()
    cursor.close()
    conn.close()


def get_batsmen():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name, fours, sixes, strkrate FROM batsmen")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data