import json
import requests

with open("server_params.json", "r") as file:
    data = json.loads(file.read())

print(data)
name_server = "http://" + data["server"] + ":" + data["port"]
print(name_server)
json2 = requests.get(name_server).json()
n = len(json2['self'])
print(round(sum([(x ** 2 - y ** 2) ** 2 for x, y in zip(json2['self'], json2['others'])]) / n, 2))