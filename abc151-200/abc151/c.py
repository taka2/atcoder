# -*- coding: utf-8 -*-
from collections import defaultdict

N,M = map(int, input().split())
pS = []
for i in range(M):
    p,S = input().split()
    p = int(p)
    pS.append((p,S))

acMap = defaultdict(int)
waMap = defaultdict(int)

for i in range(M):
    p,S = pS[i]
    if S == "AC":
        acMap[p] = 1
    else:
        if p not in acMap:
            waMap[p] += 1

acCount = len(acMap)
waCount = 0
for waElem in waMap:
    if waElem in acMap:
        waCount += waMap[waElem]

print(acCount, waCount)