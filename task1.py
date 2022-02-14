import json
import sys


ans = {"desires": {},
       "opportunities": {}}
text = sys.stdin.readlines()
for line in text:
    key, value = line.strip().split(" = ")
    if len(value) <= 8:
        ans["opportunities"][key] = value
    else:
        ans["desires"][key] = value

with open("looking_for.json", "w") as file:
    json.dump(ans, file)