# -*- coding: utf-8 -*-
from collections import defaultdict

N = int(input())
S = []
for i in range(N):
    S.append(input())

mapAns = defaultdict(int)
for i in range(N):
    Si = S[i]
    mapAns[Si] += 1

print("AC x", mapAns["AC"])
print("WA x", mapAns["WA"])
print("TLE x", mapAns["TLE"])
print("RE x", mapAns["RE"])