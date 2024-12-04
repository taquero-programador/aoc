# aoc day 1-1

import csv

a = []
b = []

#res = 0
#for x, y in sorted(zip(a, b)):
#    res += y - x
    #print(f"{x}, {y}. Largo: {y-x}")
    #print(res)


path = r"input01.txt"

with open(path, encoding="utf-8-sig") as f:
    lec = csv.reader(f)
    for i in lec:
        for n in i:
            x, y = n.split()
            a.append(int(x))
            b.append(int(y))

res = 0
for x, y in zip(sorted(a), sorted(b)):
    res += abs(y - x)

print(res)
