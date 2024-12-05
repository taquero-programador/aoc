#!/bin/python

import csv

res = []
with open(r"output.txt", "r", encoding="utf-8-sig") as file:
    lec = csv.reader(file)
    for x, y in lec:
        print(f"{x}*{y}: {int(x)*int(y)}")
        res.append(int(x)*int(y))

print(abs(sum(res)))
