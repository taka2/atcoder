# -*- coding: utf-8 -*-
N,H,X = map(int, input().split())
P = list(map(int, input().split()))

ans = -1
for i in range(N):
    if H + P[i] >= X:
        ans = i+1
        break

print(ans)