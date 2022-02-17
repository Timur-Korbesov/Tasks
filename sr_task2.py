import json
import requests

with open("desert.json", "r") as file:
    data = json.loads(file.read())

color = data["color"]
min_height = int(data["min_height"])
name_server = "http://" + data["host"] + ":" + data["port"]
json2 = requests.get(name_server).json()
lst = []

for v in json2:
    if v["color"] == color and v["height"] >= min_height:
        for el in sorted(v["shades"]):
            add_line = f"{v['height']},{v['duration']},{el}\n"
            lst.append(add_line)

lst = list(set(lst))
lst.sort(key=(lambda x: (-int(x.split(",")[0]), x.split(",")[-1])))
with open("dune_colors.csv", "w") as file:
    file.write("height,length,shade\n")
    for line in lst:
        file.write(line)
file.close()