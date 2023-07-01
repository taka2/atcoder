# -*- coding: utf-8 -*-
N,M = map(int, input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int, input().split()))

defaultPrice = P[0]
priceMap = {}
for i in range(M):
    priceMap[D[i]] = P[i+1]

ans = 0
for i in range(N):
    if C[i] in priceMap:
        ans += priceMap[C[i]]
    else:
        ans += defaultPrice

print(ans)