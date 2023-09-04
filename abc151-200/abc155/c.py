# -*- coding: utf-8 -*-
from collections import defaultdict

N = int(input())
S = []
for i in range(N):
    S.append(input())

mapS = defaultdict(int)

for i in range(N):
    mapS[S[i]] += 1

maxCount = 0
for keyMapS in mapS:
    maxCount = max(maxCount, mapS[keyMapS])

ansList = []
for keyMapS in mapS:
    if mapS[keyMapS] == maxCount:
        ansList.append(keyMapS)

ans = sorted(ansList)
for i in range(len(ans)):
    print(ans[i])