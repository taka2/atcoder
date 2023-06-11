# -*- coding: utf-8 -*-
from collections import defaultdict

N,Q = map(int, input().split())
a = list(map(int, input().split()))
xk = []
for i in range(Q):
    (x,k) = map(int, input().split())
    xk.append((x,k))

mapa = defaultdict(list)
for i in range(N):
    mapa[a[i]].append(i+1)

for i in range(Q):
    (x,k) = xk[i]
    if x in mapa and k <= len(mapa[x]):
        print(mapa[x][k-1])
    else:
        print("-1")