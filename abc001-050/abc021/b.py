# -*- coding: utf-8 -*-
N = int(input())
a,b = map(int, input().split())
K = int(input())
P = list(map(int, input().split()))

choufuku = False
mapChoufuku = {}
for i in range(K):
    if P[i] not in mapChoufuku:
        mapChoufuku[P[i]] = 1
    else:
        choufuku = True
        break

if choufuku or a in P or b in P:
    print("NO")
else:
    print("YES")