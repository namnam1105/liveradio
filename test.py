import json
newString = "namnam: hello excal"
with open('./client/src/lol.json', "r") as f:
    global data
    data = json.load(f)
    print(data)
    data.append(newString)
    print(data)

with open('./client/src/lol.json', "w") as f:
    json.dump(data, f)