# -*- coding: utf-8 -*-
N,M = map(int, input().split())
AB = []
for i in range(N):
    A,B = map(int, input().split())
    AB.append((A,B))

sortedAB = sorted(AB)

ans = 0
sumDrinks = 0
for i in range(N):
    zan = M-sumDrinks
    (A,B) = sortedAB[i]
    if zan > B:
        ans += A*B
        sumDrinks += B
    else:
        ans += A*zan
        sumDrinks += zan
        break

print(ans)