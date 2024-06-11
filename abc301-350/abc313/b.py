# -*- coding: utf-8 -*-
from collections import defaultdict

N,M = map(int, input().split())
AB = []
mapA = defaultdict(list)
for i in range(M):
    A,B = map(int, input().split())
    mapA[B].append(A)

emptyList = []
for i in range(1,N+1):
    if i not in mapA:
        emptyList.append(i)

if len(emptyList) == 1:
    print(emptyList[0])
else:
    print("-1")