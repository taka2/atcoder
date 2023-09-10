# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split()))

ans = 0
minA = 10**18
for i in range(N):
    minA = min(minA, A[i])
    if A[i] <= minA:
        ans += 1

print(ans)