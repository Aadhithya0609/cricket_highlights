from fastapi import FastAPI
import json
from database import conn, get_batsmen
import redis
import json
r=redis.Redis(host='localhost',port=6379,db=0)
app = FastAPI()



@app.get("/highlights")
def get_highlights():
    cached = r.get("batsmen")
    if cached:
        batsmen=json.loads(cached)
    else:
        batsmen=get_batsmen()
        r.set("batsmen",json.dumps(batsmen))

    scores = []
    print(batsmen)
    for player in batsmen:
        if player[1] > 0 or player[2] > 0:
            scores.append((player[0], player[1] * 10 + player[2] * 5+ float(player[3]) / 10))
        
    


    


    
        


    ''' wicket=[]
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
    } '''
    return {
        "top_batsmen":scores
    }
    