import sys
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('server', type=str)
parser.add_argument('port', type=str)
parser.add_argument('key', type=str)
parser.add_argument('--divide', default=1, type=int)
parser.add_argument('--largest', default=100, type=int)

args = parser.parse_args()

print(args)

print(sys.argv)
name_server = "http://" + args.server + ":" + args.port

f = open("civilization.csv", "w")

json2 = requests.get(name_server).json()
print(json2[args.key].keys())
for k in json2[args.key].keys():
    lst = json2[args.key].keys()
    lst = filter(lambda x: x <= args.largtest, lst)
    lst = list(map(lambda x: x // args.divide, args.json2[args.key][k]))
    line = ":".join(map(str, [k, max(lst), min(filter(lambda x: x > 0, lst)), sum(lst), round((sum(lst) / len(lst)), 2)]))
    print(line, file=f)
f.close()