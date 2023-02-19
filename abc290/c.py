# -*- coding: utf-8 -*-
N,K = map(int, input().split())
A = list(map(int, input().split()))

mapA = {}
for i in range(N):
    mapA[A[i]] = 1

ans = 0
for i in range(K):
    if i not in mapA:
        break
    else:
        ans += 1
print(ans)