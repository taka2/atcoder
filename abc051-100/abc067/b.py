# -*- coding: utf-8 -*-
N,K = map(int, input().split())
l = list(map(int, input().split()))

sortedL = sorted(l, reverse=True)
ans = 0
for i in range(K):
    ans += sortedL[i]

print(ans)