# -*- coding: utf-8 -*-
H,W = map(int, input().split())
A = []
minvalue = 100
for i in range(H):
    row = list(map(int, input().split()))
    minvalue = min(minvalue, min(row))
    A.append(row)

ans = 0
for i in range(H):
    for j in range(W):
        ans += (A[i][j] - minvalue)

print(ans)