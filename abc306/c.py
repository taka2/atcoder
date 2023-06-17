# -*- coding: utf-8 -*-
from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

mapCount = defaultdict(int)
mapPos = defaultdict(int)

for i in range(N*3):
    Ai = A[i]
    mapCount[Ai] += 1
    if mapCount[Ai] == 2:
        mapPos[Ai] = i+1

ansList = []
for i in range(1,N+1):
    ansList.append((i, mapPos[i]))

ans = sorted(ansList, key=lambda x: x[1])

ansa = []
for i in ans:
    ansa.append(i[0])

print(*ansa)