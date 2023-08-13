# -*- coding: utf-8 -*-
N,K = map(int, input().split())
p = list(map(int, input().split()))

sortedP = sorted(p)

ans = 0
for i in range(K):
    ans += sortedP[i]

print(ans)