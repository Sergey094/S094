import json

j = "{"students": [{"name": "Ann", "score": 75},{"name": "Bob", "score": 90},{"name": "Clara", "score": 60},{"name": "Dan", "score": 82}]}"

p = json.loads(j)

a = []

for st in p["students"]:
    if st["score"] >= 75:
        st["score"] = int(st["score"] * 1.1)
        a.append(st)

