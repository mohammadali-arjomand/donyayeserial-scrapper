import requests as req
import json

with open("API_KEY", "r") as file:
    apikeys = file.read().split("\n")
    print(f"{len(apikeys)} ApiKeys found")

counter = 0
act = 0
notact = 0
nactives = []
for key in apikeys:
    counter+=1
    r = req.get(f"http://www.omdbapi.com/?i=tt3896198&apikey={key}")
    if json.loads(r.text)["Response"] == "True":
        act += 1
        print(f"[{counter}] active")
    else:
        notact += 1
        nactives.append(key)
        print(f"[{counter}] NOT active")

print("\nREPORT:")
print(f"Active ApiKeys: {act}/{len(apikeys)}")
print(f"Not Active ApiKeys: {notact}/{len(apikeys)}")
if notact == 0:
    print("Congratulations! All of your ApiKeys are active")
else:
    print("List of Not Active ApiKeys:")
    for na in nactives:
        print(na)
