# -*- coding: utf-8 -*-
N,T = map(int, input().split())
A = []
for i in range(N):
    A.append(int(input()))

ans = 0
prevto = -1
for i in range(N):
    fromnum = A[i]
    tonum = fromnum + T
    if fromnum < prevto:
        fromnum = prevto
    ans += tonum - fromnum
    prevto = tonum

print(ans)