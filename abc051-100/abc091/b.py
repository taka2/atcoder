# -*- coding: utf-8 -*-
from collections import defaultdict

N = int(input())
mapS = defaultdict(int)
for i in range(N):
    mapS[input()] += 1
M = int(input())
mapT = defaultdict(int)
for i in range(M):
    mapT[input()] += 1

ans = 0
for keyS in mapS:
    sum = mapS[keyS] - mapT[keyS]
    ans = max(ans, sum)

print(ans)