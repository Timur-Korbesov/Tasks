import sys
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('host', type=str)
parser.add_argument('port', type=str)
parser.add_argument('index', type=int, nargs="+")
parser.add_argument('--letter', default="a", type=str)
parser.add_argument('--dist', default=100, type=int)

args = parser.parse_args()

print(sys.argv)
name_server = "http://" + args.server + ":" + args.port

f = open("civilization.csv", "w")

json2 = requests.get(name_server).json()
print(json2[args.key].keys())
ans = json2[0][0]
res = [{}]
for i in range(len(ans)):
    if i in args.index:
        lst = filter(lambda x: x[1] <= args.dist and args.letter in x[0], ans[i])
        minimum = 100000
        maximum = -1
        for l in lst:
            minimum = min(l[1], minimum)
            res[0]["index"] = i
            res[1]["nearest"] = minimum
            maximum = max(l[1], maximum)

        print('', file=f)
    else:
        break
f.close()