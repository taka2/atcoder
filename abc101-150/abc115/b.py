# -*- coding: utf-8 -*-
N = int(input())

p = []
for i in range(N):
    p.append(int(input()))

sortedP = sorted(p, reverse=True)

ans = sortedP[0] // 2
for i in range(1,N):
    ans += sortedP[i]

print(ans)