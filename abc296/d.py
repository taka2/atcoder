# -*- coding: utf-8 -*-
N,M = map(int, input().split())

ans = 2*10**18
for i in range(1,N+1):
    X = (M+i-1)//i
    if X <= N:
        ans = min(ans, i*X)
    if i > X:
        break

if ans == 2*10**18:
    print("-1")
else:
    print(ans)