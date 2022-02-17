import json
import sys


ans = {"England": {}, "France": {}, "Channel": {}}
text = sys.stdin.readlines()
for line in text:
    key, key_2, value = line.strip().split(", ")
    if key_2 not in ans[key]:
        ans[key][key_2] = int(value)
    else:
        ans[key][key_2] += int(value)

with open("observations.json", "w") as file:
    json.dump(ans, file)