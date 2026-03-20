from fastapi import FastAPI
import json

app = FastAPI()

with open("sample.json") as f:
    data = json.load(f)

@app.get("/highlights")
def get_highlights():
    batsmen = data["scorecard"][0]["batsman"]
    bowlers = data["scorecard"][0]["bowler"]
    fow = data["scorecard"][0]["fow"]["fow"]
    scores = []

    for player in batsmen:
        if player["sixes"] > 0 or player["fours"] > 0:
            scores.append((player["name"], player["sixes"] * 10 + player["fours"] * 5))


    


    
        


    wicket=[]
    for player1 in bowlers:
        excitement=player1["wickets"] *10
        wicket.append((player1["name"],excitement))
    
    
        
    moments=[]
    for i in fow:
        parts = str(i["overnbr"]).split(".")
        over = parts[0]
        ball = parts[1]
        moments.append((i["batsmanname"], over, ball, i["runs"]))

    return {
        "top_batsmen": scores,
        "top_bowlers": wicket,
        "wicket_moments": moments
    }