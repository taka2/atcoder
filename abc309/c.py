# -*- coding: utf-8 -*-
from collections import defaultdict

N,K = map(int, input().split())
ab = []
for i in range(N):
    a,b = map(int, input().split())
    ab.append((a,b))

mapAB = defaultdict(int)
for i in range(N):
    (a,b) = ab[i]
    mapAB[a] += b

sumMapAB = defaultdict(int)
sum = 0
for key in sorted(list(mapAB), reverse=True):
    sum += mapAB[key]
    sumMapAB[key] = sum

prevKey = 0
for key in sorted(list(sumMapAB)):
    if sumMapAB[key] <= K:
        print(prevKey+1)
        exit(0)
    prevKey = key

print(prevKey+1)