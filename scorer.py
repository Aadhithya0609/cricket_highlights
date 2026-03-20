import json
with open("sample.json") as f:
    data=json.load(f)
batsmen = data["scorecard"][0]["batsman"]
bowlers = data["scorecard"][0]["bowler"]
fow=data["scorecard"][0]["fow"]["fow"]



scores = []

for player in batsmen:
    excitement = player["sixes"] * 10 + player["fours"] * 5 + float(player["strkrate"]) / 10
    scores.append((player["name"], excitement))


scores.sort(key=lambda x: x[1], reverse=True)


for name, score in scores[:3]:
    print(name, score)


wicket=[]
for player1 in bowlers:
    excitement=player1["wickets"] *10
    wicket.append((player1["name"],excitement))
wicket.sort(key=lambda x:x[1],reverse=True)
for name,wickets in wicket[:2]:
    print(name,wickets)

for i in fow:
    parts = str(i["overnbr"]).split(".")
    over = parts[0]
    ball = parts[1]
    print(i["batsmanname"], "Over", over, "Ball", ball, "Score", i["runs"])
