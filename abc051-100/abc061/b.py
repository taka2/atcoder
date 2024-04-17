# -*- coding: utf-8 -*-
from collections import defaultdict

N,M = map(int, input().split())
mapAB = defaultdict(int)
for i in range(M):
    a,b = map(int, input().split())
    mapAB[a] += 1
    mapAB[b] += 1

for i in range(N):
    print(mapAB[i+1])