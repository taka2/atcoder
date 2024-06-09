# -*- coding: utf-8 -*-
N,T = map(int, input().split())
ct = []
for i in range(N):
    (c,t) = map(int, input().split())
    ct.append((c,t))

ans = 999999
for i in range(N):
    (c,t) = ct[i]
    if t <= T:
        ans = min(ans, c)

if ans == 999999:
    print("TLE")
else:
    print(ans)