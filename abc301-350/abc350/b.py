# -*- coding: utf-8 -*-
N,Q = map(int, input().split())
T = list(map(int, input().split()))

listT = [0] + [1] * N
for i in range(Q):
    if listT[T[i]] == 1:
        listT[T[i]] = 0
    else:
        listT[T[i]] = 1

ans = 0
for i in range(N+1):
    if listT[i] == 1:
        ans += 1

print(ans)